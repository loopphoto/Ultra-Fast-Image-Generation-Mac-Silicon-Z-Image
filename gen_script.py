from gradio_client import Client, handle_file
from pathlib import Path
import shutil
import uuid

client = Client("http://127.0.0.1:7860/")
seed = -1
steps = 7
result = client.predict(
	prompt=(
		"Outdoor candid lifestyle photograph of an adult woman sitting on a towel-covered beach lounger on a sunny white-sand beach, relaxed casual posture with legs apart, head tilted slightly downward. "
		"She wears a light green minimalist string bikini with thin straps, a dark green baseball cap with white embroidered lettering, and dark sunglasses, holding a fresh coconut with both hands while drinking through a straw. "
		"Bright midday natural sunlight from above and slightly to the side, creating crisp shadows on the sand and body, strong highlights and clear contrast, true outdoor coastal lighting. "
		"Vacation travel photography aesthetic, unposed and authentic, natural body proportions, realistic skin texture with subtle sun sheen, no glamour retouching. "
		"Textured white sand and beach loungers in the foreground, turquoise ocean waves and swimmers in the background, clear blue sky with distant clouds, photorealistic, high detail, sharp focus, 4k quality."
	),
	height=512,
	width=512,
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
