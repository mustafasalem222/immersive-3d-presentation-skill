# Huashu Design principles adapted for presentation work

Source reviewed: https://github.com/alchaincyf/huashu-design

This note records the parts integrated into `SKILL.md`; it is not a copy of the upstream repository.

## Adopted principles

1. **Design context before styling.** Inspect existing brand assets, source content, screenshots, UI and references. Do not invent brand identity when authentic material exists.
2. **Three visual directions.** New visual work begins with three materially different concept boards. A multi-slide deck uses two representative slides per direction; the user chooses before full production. Explicitly requested immediate execution and already-approved iterations are exceptions.
3. **Real assets matter.** For named products/brands, seek official logos, product imagery, UI captures and published brand specifications. Mark missing assets honestly.
4. **Form follows content.** Each slide answers its narrative role, viewing distance, emotional temperature, capacity and subject-specific visual metaphor.
5. **Anti-AI-slop.** Avoid generic purple gradients, emoji iconography, repetitive card layouts, fake stats and stock decoration. These may be used only when justified by the actual brand or subject.
6. **Junior-designer checkpoints.** Surface assumptions and representative slides early; validate the visual grammar before building a long deck.
7. **Cinematic continuity.** Prefer a persistent hero motif and evolving spatial narrative over disconnected transitions.
8. **Critique before delivery.** Review conceptual coherence, hierarchy, craft, functionality and originality; provide Keep/Fix/Quick Wins.
9. **Export honestly.** HTML is the visual master. PDF and PPTX are derivatives; explain loss of 3D, animation or editability rather than compromising the master.
10. **Verify factual claims.** Search authoritative current sources for changing product facts and statistics; cite them in the deck.

## Deliberate reconciliation with the immersive engine

- Huashu's direction gate is used before the immersive engine's full deck build. Once a direction is approved, the engine's 3D, RTL, interaction and accessibility requirements become mandatory.
- The immersive engine's single-file template is retained as the default for portable decks. Larger decks may use a multi-file architecture if a reliable overview/navigation shell is supplied.
- The three.js layer is a presentation enhancement, not a replacement for HTML text, charts, controls or accessible interactions.
- The interaction contract is mandatory even if the chosen concept is visually restrained. When WebGL is unavailable, CSS-3D and all non-WebGL interactions remain functional.
- The Huashu source describes broader design, prototype and motion workflows. This merged skill intentionally scopes those ideas to presentation decks rather than claiming to reproduce every Huashu capability.

## License and attribution

The upstream repository README states that Huashu Design has been MIT licensed since 2026-05-14. If copying upstream code/assets in a future extension, include the upstream MIT license and copyright notice. The present package adapts principles and does not include Huashu's code/assets.
