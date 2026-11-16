# Image prompts

An image model draws what the words describe. Describe the picture the way a photographer or illustrator would brief someone. Ask 2 to 3 question or refrence image if some scene, details or requiremnts are not clear or confusing or conflecting. The Goal is to produce expected image in one go.

## Order

Write one or two sentences in this order. Skip what doesn't matter.

1. **Subject:** what is in the picture, with 2–3 concrete details ("a glass of masala chai with a thin layer of foam").
2. **Setting:** where it is ("on a stone window sill in an old Mumbai flat").
3. **Light:** the single biggest change you can make (see below).
4. **Camera and framing:** distance, angle, lens feel.
5. **Style:** photo, watercolour, flat vector, 3D render, pencil sketch, and so on.
6. **Mood or colour palette** if it matters.
7. **Text in the image:** write the exact words in quotes and say where they go. Keep it short.

Set size and aspect ratio (square, portrait 9:16, landscape 16:9) in the tool's own setting when it has one. If it has none, say it in words: "vertical 9:16 composition".

## Light words that change the picture

| Words | What you get |
|---|---|
| warm sunset light from the side, long soft shadows | Golden-hour look |
| soft overcast daylight | Even, gentle, no harsh shadows |
| harsh midday sun, hard shadows | Strong contrast |
| window light from the left | Natural indoor portrait light |
| neon signs reflecting on wet streets | Night city glow |
| studio lighting, white seamless background | Clean product shot |
| backlit, rim light around the hair | Subject separated from the background |

## Camera and framing words

close-up · extreme close-up · wide shot · bird's-eye view · low angle looking up · eye level · shallow depth of field (blurred background) · macro · centred composition · rule-of-thirds composition · lots of empty space on the right for text

## What does not work (and what to do instead)

| People write | What happens | Write instead |
|---|---|---|
| `/8k`, `8k`, `4k`, `ultra HD` | Does not set the file's resolution. The tool decides the pixel size (in one test, an image asked for with "/8k" came out 1672 × 941, the same as without it) | Choose size in the tool's settings; ask for "fine detail, sharp focus" if you want detail |
| `masterpiece`, `best quality`, `trending on artstation` | Vague; tells the model nothing about what you actually want | Describe the actual quality: "sharp focus, natural skin texture, accurate hands" |
| `/golden hour` | Works only because "golden hour" is a real phrase; the slash adds nothing | "warm golden-hour light, low sun" |
| A long list of 30 keywords | The model drops some and mixes others | 1–3 clear sentences |
| Many negative words ("no blur, no text, no people") | Can backfire: naming a thing can put it in the picture | Describe what you want instead; use the tool's negative-prompt field if it has one |

## Example

Rough: "chai ki photo chahiye instagram ke liye, sunset wali"

Prompt:
```
A glass of masala chai with light foam on a stone window sill, a money plant in a clay pot beside it, city rooftops softly blurred outside. Warm sunset light from the side with long soft shadows. Eye-level close-up, shallow depth of field. Realistic photo, warm orange and brown tones. Vertical 4:5 composition with empty space at the top for a caption.
```

Kyun:
- Light described in plain words ("warm sunset light from the side"), so the golden look is reliable.
- Framing and aspect ratio stated, so it fits an Instagram post.
- Empty space asked for, so text can go on top later.
