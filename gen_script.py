from gradio_client import Client, handle_file
from pathlib import Path
import shutil
import uuid

client = Client("http://127.0.0.1:7860/")
seed = -128
steps = 5
result = client.predict(
	prompt=(
		"Outdoor candid street-style photograph of a slim adult woman in her early twenties (21–22), walking confidently along a sunny city sidewalk, relaxed but subtly flirtatious posture, soft smile while glancing slightly downward. "
		"She wears a fitted light grey sleeveless tank top that contours her busty body and shows cleavage and midriff, and low-slung dark navy jogger-style pants, emphasizing her waist and hips, carrying a light canvas tote over one shoulder and holding a green iced drink in her hand. "
		"Long blonde hair worn loose with a center part, glossy natural texture, small oval sunglasses, minimal jewelry including a delicate necklace resting at the collarbone, effortless attractive styling. "
		"Bright midday natural sunlight creating gentle highlights on skin and soft shadows that accentuate natural curves, realistic outdoor urban lighting with no artificial flash. "
		"Urban street background with parked cars, storefronts, and road markings, medium depth of field keeping focus on the subject, modern lifestyle fashion aesthetic. "
		"Confident youthful energy, natural body proportions, realistic skin texture with subtle warmth, photorealistic, sharp focus, high detail, 4k quality."
	),
	height=1024,
	width=1024,
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
