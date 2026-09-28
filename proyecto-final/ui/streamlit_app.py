from pathlib import Path

import httpx
import streamlit as st


ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = ROOT / "data"

st.set_page_config(page_title="Asistente de IA", page_icon="📚")
st.title("Asistente de apuntes de IA")
st.caption("Las respuestas se generan usando solamente los documentos indexados.")

api_url = st.sidebar.text_input("Dirección de la API", "http://localhost:8000")

try:
    health = httpx.get(f"{api_url}/health", timeout=5).json()
    st.sidebar.success(f"API conectada · {health['chunks']} chunks")
    if not health["api_key_configured"]:
        st.sidebar.warning("Falta configurar GOOGLE_API_KEY")
except Exception:
    health = None
    st.sidebar.error("La API no está disponible")

tab_documents, tab_questions = st.tabs(["Documentos", "Preguntar"])

with tab_documents:
    st.subheader("Indexar documentos")
    st.write("Puedes usar los seis apuntes incluidos o cargar archivos PDF, TXT y Markdown.")

    if st.button("Indexar corpus incluido", use_container_width=True):
        paths = sorted(DATA_DIR.glob("*.md"))
        files = [("files", (path.name, path.read_bytes(), "text/markdown")) for path in paths]
        try:
            response = httpx.post(f"{api_url}/ingest", files=files, timeout=180)
            response.raise_for_status()
            result = response.json()
            st.success(f"Se indexaron {result['documents']} documentos y {result['chunks']} chunks.")
        except Exception as error:
            detail = getattr(getattr(error, "response", None), "text", str(error))
            st.error(f"No se pudo indexar: {detail}")

    uploaded = st.file_uploader(
        "O carga tus propios archivos",
        type=["pdf", "txt", "md"],
        accept_multiple_files=True,
    )
    if st.button("Indexar archivos seleccionados", disabled=not uploaded):
        files = [("files", (file.name, file.getvalue(), file.type)) for file in uploaded]
        try:
            response = httpx.post(f"{api_url}/ingest", files=files, timeout=180)
            response.raise_for_status()
            result = response.json()
            st.success(f"Se indexaron {result['documents']} documentos y {result['chunks']} chunks.")
        except Exception as error:
            detail = getattr(getattr(error, "response", None), "text", str(error))
            st.error(f"No se pudo indexar: {detail}")

with tab_questions:
    st.subheader("Consultar el corpus")
    question = st.text_input("Pregunta", placeholder="¿Qué diferencia hay entre BFS y DFS?")
    top_k = st.slider("Fragmentos a recuperar", 2, 5, 3)

    if st.button("Preguntar", type="primary", disabled=not question.strip()):
        try:
            response = httpx.post(
                f"{api_url}/query",
                json={"question": question, "top_k": top_k},
                timeout=90,
            )
            response.raise_for_status()
            result = response.json()

            if result["abstained"]:
                st.warning(result["answer"])
            else:
                st.success(result["answer"])

            st.markdown("#### Evidencia recuperada")
            for number, item in enumerate(result["citations"], start=1):
                label = f"[{number}] {item['source']} · score {item['score']:.3f}"
                with st.expander(label):
                    st.write(item["text"])
        except Exception as error:
            detail = getattr(getattr(error, "response", None), "text", str(error))
            st.error(f"No se pudo responder: {detail}")

