# Higgsfield-Katalog (automatisch)

Erzeugt 18.10.2026 mit `tools/katalog.py` direkt aus der Higgsfield-CLI. Nur was die CLI meldet. Achtung: Manche Fähigkeiten stehen nicht als Parameter da (z. B. erzeugt Veo 3.1 Ton und Dialog nativ, ohne Schalter). Bei Zweifeln `higgsfield model get <job_type>` und die offizielle Seite prüfen.

## Video (42 Modelle)

| job_type | Name | Fähigkeiten laut CLI | Regeln |
|---|---|---|---|
| `ad_multiplier` | Ad Multiplier | Dauer frei (Std. 5) s; Auflösung 480p/720p/1080p; Ton an/aus; Audio-Referenzen; Startbild; Endbild; Bild-Referenzen; Video-Referenzen; mode: t2v/omni_reference/video_edit/video_extension; max 30 Bilder | mode 't2v' does not accept reference media · mode 'omni_reference' requires at least one reference media item · at most 50 reference media items are allowed in total · mode 'video_edit' requires exactly one video reference · mode 'video_extension' requires at  |
| `ad_multiplier_v2` | Ad Multiplier Recreate | Auflösung 480p/720p/1080p; Bild-Referenzen; Video-Referenzen; mode: recreate/sections | exactly one video_references entry is required · section is required when mode is sections · section is only allowed when mode is sections |
| `bytedance_video_upscale` | Bytedance Video Upscale | Auflösung 1080p/2k/4k; Video-Referenzen; preset: common/aigc/short_series/ugc/old_film | - |
| `clipify` | Clipify | - | provide exactly one YouTube URL per Clipify job |
| `depth_anything_video` | Depth Anything Video | Auflösung auto/360p/480p/720p/1080p; Video-Referenzen; variant: VDA-Small/VDA-Base/VDA-Large | - |
| `flux_3_video` | FLUX 3 Video | Dauer frei (Std. 5) s; Auflösung 720p/1080p/2k/4k; Ton an/aus; Startbild; Endbild; Bild-Referenzen; Video-Referenzen; max 10 Bilder | at most 10 images are allowed across start_image, image_references, and end_image · image inputs and video_references cannot be mixed · end_image requires start_image |
| `flux_3_video_edit` | FLUX 3 Video Edit | Video-Referenzen | - |
| `fps_boost` | FPS Boost | Video-Referenzen; variant: bytedance/topaz | fps below 24 is only supported with variant "topaz" |
| `gemini_omni` | Gemini Omni Flash | Dauer frei (Std. 8) s; Auflösung 720p; Bild-Referenzen; Video-Referenzen | at most 1 video_references entry is allowed · when a video reference is provided, at most 5 image_references are allowed · at most 7 image_references are allowed |
| `gemini_omni_flash_1_1` | Gemini Omni Flash 1.1 | Dauer frei (Std. 8) s; Auflösung 360p/720p/1080p/4k; Startbild; Endbild; Bild-Referenzen; Video-Referenzen; mode: text-to-video/image-to-video/reference-to-video/edit | mode 'text-to-video' does not accept media · mode 'image-to-video' requires start_image, accepts an optional end_image, and does not accept reference media · mode 'reference-to-video' requires at least one image_references or video_references item and does not |
| `hf_mult_motion_control` | Genjutsu | Auflösung 480p/720p/1080p; Bild-Referenzen; Video-Referenzen | at least one image_references entry is required · exactly one video_references entry is required |
| `hf_mult_replace_object` | Genjutsu | Auflösung 480p/720p/1080p; Bild-Referenzen; Video-Referenzen | at least one image_references entry is required · exactly one video_references entry is required |
| `veo3` | Google Veo 3 | Startbild; variant: veo-3-preview/veo-3-fast | - |
| `veo3_1` | Google Veo 3.1 | Dauer 4/6/8 s; Startbild; variant: veo-3-1-preview/veo-3-1-fast; quality: basic/high/ultra | - |
| `veo3_1_lite` | Google Veo 3.1 Lite | Dauer 4/6/8 s; Ton an/aus; Startbild; Endbild | duration must be 8 when both start_image and end_image are set |
| `grok_video_v15_lite` | Grok Imagine Video 1.5 Lite | Dauer frei (Std. 5) s; Auflösung 480p/720p/1080p; Startbild | - |
| `grok_video` | Grok Video | Dauer frei (Std. 5) s; Startbild | - |
| `grok_video_v15` | Grok Video 1.5 | Dauer frei (Std. 5) s; Auflösung 480p/720p/1080p; Audio-Referenzen; Startbild; Bild-Referenzen | start_image cannot be combined with reference media · audio_references require at least one image reference · 1080p is not available with reference media |
| `happy_horse_video` | Happy Horse Video | Dauer frei (Std. 5) s; Auflösung 720p/1080p; Startbild | - |
| `kling2_6` | Kling 2.6 Video | Dauer 5/10 s; Ton an/aus; Startbild | - |
| `kling_o3_image_reference` | Kling 3.0 Omni | Dauer frei (Std. 5) s; Ton an/aus; Bild-Referenzen; Multi-Shot; mode: std/pro/4k | Provide multi_prompt exactly when multi_shots is true. |
| `kling_o3_flf` | Kling 3.0 Omni (Frames) | Dauer frei (Std. 5) s; Ton an/aus; Startbild; Endbild; Multi-Shot; mode: std/pro/4k | Provide multi_prompt exactly when multi_shots is true. · end_image requires start_image. |
| `kling_video_edit` | Kling 3.0 Omni Edit | Bild-Referenzen; Video-Referenzen; mode: std/pro/4k | - |
| `kling3_0_turbo` | Kling 3.0 Turbo | Dauer frei (Std. 5) s; Auflösung 720p/1080p; Startbild | - |
| `kling3_0` | Kling v3.0 | Dauer frei (Std. 5) s; Ton an/aus; Startbild; Endbild; mode: std/pro/4k | - |
| `minimax_h3` | MiniMax H3 | Dauer frei (Std. 5) s; Auflösung 2K; Audio-Referenzen; Startbild; Endbild; Bild-Referenzen; Video-Referenzen | end_image requires start_image · start_image/end_image cannot be mixed with reference media · audio_references require at least one image or video reference |
| `minimax_h3_max` | MiniMax H3 Max | Dauer frei (Std. 5) s; Auflösung 480p/768p; Audio-Referenzen; Startbild; Endbild; Bild-Referenzen; Video-Referenzen | end_image requires start_image · reference media cannot be mixed with start_image or end_image · at most 12 reference media items are allowed in total · reference audio requires a reference image or video |
| `minimax_hailuo` | Minimax Hailuo | Dauer 6/10 s; Auflösung 512/768/1080; Startbild; Endbild; variant: minimax/minimax-fast/minimax-2.3/minimax-2.3-fast | resolution '512' is incompatible with end_image · resolution '512' is not supported for 'minimax-2.3' or 'minimax-2.3-fast' · resolution '1080' is not available for 10 second duration · start_image or end_image is required unless variant is 'minimax-2.3' · end |
| `sam_3_video` | Remove Background | Video-Referenzen | exactly one video_references entry is required |
| `seedance1_5` | Seedance 1.5 Pro | Dauer 4/8/12 s; Auflösung 480p/720p/1080p; Ton an/aus; Startbild; Endbild | end_image requires start_image to be set |
| `seedance_2_0` | Seedance 2.0 | Dauer frei (Std. 5) s; Auflösung 480p/720p/1080p/4k; Ton an/aus; Audio-Referenzen; Startbild; Endbild; Bild-Referenzen; Video-Referenzen; mode: std/fast | at most 9 image references are allowed (counting start_image and end_image) · at most 3 video_references are allowed · at most 3 audio_references are allowed · at most 12 reference files are allowed in total across images, videos, and audios (including start_i |
| `seedance_2_0_mini` | Seedance 2.0 Mini | Dauer frei (Std. 5) s; Auflösung 480p/720p; Ton an/aus; Audio-Referenzen; Startbild; Endbild; Bild-Referenzen; Video-Referenzen | at most 9 image references are allowed (counting start_image and end_image) · at most 3 video_references are allowed · at most 3 audio_references are allowed · at most 12 reference files are allowed in total across images, videos, and audios (including start_i |
| `seedance_2_5` | Seedance 2.5 | Dauer frei (Std. 5) s; Auflösung 480p/720p/1080p; Ton an/aus; Audio-Referenzen; Startbild; Endbild; Bild-Referenzen; Video-Referenzen; Entwurf; mode: t2v/omni_reference/video_edit/video_extension; max 30 Bilder | mode 't2v' does not accept reference media · mode 'omni_reference' requires at least one reference media item · at most 50 reference media items are allowed in total · mode 'video_edit' requires exactly one video reference · mode 'video_extension' requires at  |
| `topaz_video` | Topaz | Auflösung 1080p/2160p; Video-Referenzen | - |
| `topaz_hyperion_2_5` | Topaz Hyperion 2.5 | Video-Referenzen | - |
| `video_background_remover` | Video Background Remover | Video-Referenzen | exactly one video is required in video_references |
| `video_deflicker` | Video Deflicker | Dauer frei (Std. None) s | - |
| `video_upscale` | Video Upscale | Dauer frei (Std. None) s | - |
| `wan2_6` | Wan 2.6 Video | Dauer 5/10/15 s; Audio-Referenzen; Bild-Referenzen; Video-Referenzen; quality: 720p/1080p | reference-to-video (with video_references) supports only 5 or 10 second durations |
| `wan2_7` | Wan 2.7 | Dauer frei (Std. 5) s; Auflösung 720p/1080p; Audio-Referenzen; Startbild; Endbild | end_image requires start_image · at most 1 audio reference is allowed |
| `wan3_0` | Wan 3.0 | Dauer frei (Std. 5) s; Auflösung 480p/720p/1080p; Ton an/aus; Audio-Referenzen; Startbild; Endbild; Bild-Referenzen; Video-Referenzen | end_image requires start_image · start_image/end_image cannot be combined with reference media · duration must be -1 (smart duration) or between 2 and 30 |
| `wan3_0_prime` | Wan 3.0 Prime | Dauer frei (Std. 5) s; Auflösung 480p/720p/1080p; Ton an/aus; Audio-Referenzen; Startbild; Endbild; Bild-Referenzen; Video-Referenzen | end_image requires start_image · start_image/end_image cannot be combined with reference media · duration must be -1 (smart duration) or between 2 and 30 |

## Image (39 Modelle)

| job_type | Name | Fähigkeiten laut CLI | Regeln |
|---|---|---|---|
| `3d_jutsu_angles` | 3D Jutsu Angles | Auflösung 1k/1.5k/2k; Bild-Referenzen | at most 10 image_references are allowed |
| `autosprite` | AutoSprite Animation | Bild-Referenzen | prompt and name are required when kind is custom · prompt and name are only supported when kind is custom |
| `bytedance_image_upscale` | Bytedance Image Upscale | Auflösung 2k/4k; Bild-Referenzen | exactly one image_references entry is required |
| `flux_3_image` | FLUX 3 Image | Auflösung 768sq/1k/1.5k/2k/4k; Bild-Referenzen | - |
| `flux_2` | FLUX.2 | Auflösung 1k/2k; Bild-Referenzen; variant: pro/flex/max | - |
| `flux_2_pro_outpaint` | FLUX.2 Pro Outpaint | Bild-Referenzen | exactly one image_references entry is required · at least one expand side must be non-zero |
| `flux_kontext` | Flux Kontext | Bild-Referenzen | at most 4 image_references are allowed |
| `gpt_image_2` | GPT Image 2 | Auflösung 1k/2k/4k; Bild-Referenzen; quality: low/medium/high | - |
| `gpt_image_2_5` | GPT Image 2.5 | Auflösung 1k/2k/4k; Bild-Referenzen; variant: flare/sunburst; quality: low/medium/high/xhigh/max | - |
| `grok_image` | Grok Image | Auflösung 1k/2k; Bild-Referenzen; mode: std/quality | - |
| `grok_image_2_0` | Grok Image 2.0 | Auflösung 1k/2k; Bild-Referenzen; quality: low/medium | - |
| `text2image_soul_v2` | Higgsfield Soul 2.0 | Bild-Referenzen; quality: 1.5k/2k | at most one image reference is allowed · style_id cannot be combined with image_references |
| `ideogram_4_5` | Ideogram 4.5 | Auflösung 1k/2k; Bild-Referenzen; quality: very_low/low/medium/high | Very low quality requires a source image. · A mask requires one to four source images. · This aspect ratio requires 2K resolution without a mask. |
| `image_auto` | Image Auto | Bild-Referenzen | at most 14 image references are allowed |
| `image_background_remover` | Image Background Remover | Bild-Referenzen | exactly one image_references entry is required |
| `kling_omni_image` | Kling O1 Image | Auflösung 1k/2k; Bild-Referenzen | at most 10 image_references are allowed · aspect_ratio 'auto' requires at least one image_reference |
| `nano_banana` | Nano Banana | Bild-Referenzen | at most 8 image_references are allowed |
| `nano_banana_flash` | Nano Banana 2 | Auflösung 1k/2k/4k; Bild-Referenzen | - |
| `nano_banana_2_lite` | Nano Banana 2 Lite | Auflösung 1k; Bild-Referenzen | a non-empty prompt or at least one image reference is required · at most 14 image references are allowed · aspect_ratio 'auto' requires at least one image reference |
| `nano_banana_2_1` | Nano Banana 2.1 | Auflösung 1k/2k/4k; Bild-Referenzen; Video-Referenzen | at most 14 image inputs including the mask are allowed · video references are not supported for region inpaint |
| `nano_banana_pro` | Nano Banana Pro | Auflösung 1k/2k/4k; Bild-Referenzen | a non-empty prompt or at least one image reference is required · at most 14 image references are allowed |
| `nano_banana_2_ai_stylist` | Nano Banana Pro | Bild-Referenzen | 'outfit_preset_ids' or 'user_outfit_ids' is required |
| `nano_banana_2_relight` | Nano Banana Pro | Bild-Referenzen | - |
| `nano_banana_2_skin_enhancer` | Nano Banana Pro | Bild-Referenzen | - |
| `nano_banana_2_shots` | Nano Banana Pro | Bild-Referenzen | 'image_references' must contain exactly one image |
| `openai_hazel` | OpenAI Hazel | Bild-Referenzen; quality: low/medium/high | aspect_ratio 'auto' requires at least one image reference · at most 16 image references are allowed |
| `outpaint` | Outpaint | Bild-Referenzen | exactly one image_references entry is required |
| `recraft_v4_styles` | Recraft V4 Styles | Auflösung 1k/2k | - |
| `recraft_v4_1` | Recraft V4.1 | Auflösung 1k/2k | Each color in colors must be a #RRGGBB hex string (six hex digits, no alpha). · background_color must be a #RRGGBB hex string (six hex digits, no alpha) or null. |
| `seedream_v4_5` | Seedream 4.5 | Bild-Referenzen; quality: basic/high | at most 14 image_references are allowed |
| `seedream_5_0_flash` | Seedream 5.0 Flash | Auflösung 1k/1.5k/2k; Bild-Referenzen | at most 10 image_references are allowed |
| `seedream_v5_lite` | Seedream 5.0 Lite | Bild-Referenzen; quality: basic/high | - |
| `seedream_v5_pro` | Seedream 5.0 Pro | Auflösung 1k/1.5k/2k; Bild-Referenzen | at most 10 image_references are allowed |
| `soul_cast` | Soul Cast | - | - |
| `soul_cinematic` | Soul Cinematic | Bild-Referenzen; quality: 1.5k/2k | at most one image reference is allowed |
| `soul_location` | Soul Location | - | - |
| `topaz_image` | Topaz | Bild-Referenzen; variant: Standard V2/Low Resolution V2/CGI/High Fidelity V2/Text Refine | - |
| `topaz_image_generative` | Topaz | Bild-Referenzen; variant: Standard MAX/Redefine/Recovery/Recovery V2 | - |
| `z_image` | Z Image | - | - |

## Audio (8 Modelle)

| job_type | Name | Fähigkeiten laut CLI | Regeln |
|---|---|---|---|
| `elevenlabs_v4` | Eleven v4 | Dialog-Eingabe | - |
| `elevenlabs_v4_turbo` | Eleven v4 Turbo | Dialog-Eingabe | - |
| `inworld_text_to_speech` | Inworld Text to Speech | - | - |
| `mirelo_text_to_audio` | Mirelo Text to Audio | Dauer frei (Std. None) s | - |
| `qwen_audio_tts` | Qwen Audio 3.0 TTS Flash | Stimme | - |
| `seed_audio` | Seed Audio 1.0 | Audio-Referenzen; Bild-Referenzen; Stimme | image_references and audio_references are mutually exclusive · voice_type and voice_id must be provided together · a voice cannot be combined with an image reference · a voice allows at most 2 additional audio references |
| `sonilo_music` | Sonilo Music | Dauer frei (Std. None) s | - |
| `text2speech_v2` | Text to Speech V2 | Stimme; variant: elevenlabs/minimax/seed_speech/vibe_voice/cozy_voice | prompt exceeds the character limit for the selected engine (elevenlabs/vibe_voice/cozy_voice: 5000, minimax: 10000, seed_speech: 15000) |

