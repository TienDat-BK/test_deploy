import gradio as gr
import numpy as np
import time

def heavy_computation(n, repeat):
    """
    Tạo ma trận nxn, nhân ma trận repeat lần.
    Trả về kết quả cuối cùng và thời gian thực thi.
    """
    n = int(n)
    repeat = int(repeat)
    start_time = time.time()

    # Tạo ma trận random
    A = np.random.rand(n, n)
    B = np.random.rand(n, n)

    result = A
    for i in range(repeat):
        result = np.dot(result, B)  # nhân ma trận nặng CPU

    elapsed = time.time() - start_time
    return f"Computation done in {elapsed:.2f} seconds", result

# Gradio UI
demo = gr.Interface(
    fn=heavy_computation,
    inputs=[
        gr.Number(label="Matrix size (n x n)", value=200, precision=0),
        gr.Number(label="Number of multiplications", value=5, precision=0)
    ],
    outputs=[
        gr.Textbox(label="Result info"),
        gr.Dataframe(label="Result matrix (showing small matrices only)")
    ],
    title="Heavy Computation Demo",
    description="This app performs repeated matrix multiplications to simulate a CPU-heavy task."
)

if __name__ == "__main__":
    demo.launch(server_name="0.0.0.0", server_port=7860)
