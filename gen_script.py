from gradio_client import Client, handle_file
from pathlib import Path
import shutil
import uuid

client = Client("http://127.0.0.1:7860/")
seed = -4000
steps = 10
result = client.predict(
	prompt=(
		"Indoor candid portrait of a young blonde adult woman sitting cross-legged on a wooden floor in a minimalist bedroom, smiling naturally toward the camera. "
		"She wears light-colored lingerie with an open striped shirt, relaxed unposed posture, intimate casual mood. "
		"Direct on-camera flash lighting creating bright highlights on skin, hard shadows on the wall and floor, slightly flattened perspective. "
		"Snapshot / point-and-shoot photography aesthetic, early-2000s film flash look, high contrast, visible texture, subtle grain. "
		"Neutral walls, unmade bed in the background, realistic proportions, photorealistic, high detail, 4k quality."
	),
	height=256,
	width=256,
	steps=steps,
	seed=seed,
	guidance=1,
	device="mps",
	lora_file=None,
	lora_strength=1,
	api_name="/generate_image"
)
print(result)
result_path = result[0] if isinstance(result, (list, tuple)) else result
output_dir = Path("gen_images")
output_dir.mkdir(exist_ok=True)
ext = Path(result_path).suffix or ".png"
out_path = output_dir / f"{seed}_{steps}_generated_{uuid.uuid4().hex}{ext}"
shutil.copy(result_path, out_path)
print(f"Generated image saved at: {out_path}")
