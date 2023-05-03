# Debugging

Error: TypeError: The keyword `fps` is no longer supported. Use `duration`(in ms) instead, e.g. `fps=50` == `duration=20` (1000 * 1/50).

Solution: Change `fps` to `duration` in the `to_gif(images)` function.
