import gradio as gr


def model_inference(image, slider_value, checkboxgroup_value):
    return f"{image}_{slider_value}_{' '.join(checkboxgroup_value)}"


title = "Title on the top center"
inputs = [
    gr.Image(),
    gr.Slider(minimum=0, maximum=9, step=1, value=3, label="Slider Info"),
    gr.CheckboxGroup(choices=['a', 'b', 'c'], value=['a', 'b'], label="CheckboxGroup Info"),
]
outputs = [
    gr.Textbox(label="Textbox Info")
]
examples = [
    ["/home/mrxir/Pictures/l3.jpg", 3, ['a', 'b']],
    ["/home/mrxir/Pictures/l8.jpg", 3, ['c']],
]

demo = gr.Interface(
    model_inference, 
    inputs=inputs,
    outputs=outputs,
    title=title,
    examples=examples
)

demo.launch(share=True)
