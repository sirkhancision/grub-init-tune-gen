## grub-init-tune-gen

This tool takes a manual input of notes and their duration and generates a code to be used in `GRUB_INIT_TUNE` at `/etc/default/grub`. The process can be quite long depending on the track. 

It doesn't support tuplets but you can work around that: say that you have a track that is comprised mostly of triplets, then you can multiply the tempo times 3/2
- grandma_nier.txt in the `examples` folder is originally a track with 107 BPM and triplets, but the tempo provided in grub-init-tune-gen was 161, because `ceiling(107 * (3/2)) = 161`, then I just typed the notes as regular 8th notes

Here are some possible inputs for notes in the program:
- E4 4 [4th note]
- f#3 2 [half note]
- f#2 1 [whole note]
- Bb6 4. [this is a dotted 4th note]
- bb4 32 [32nd note]
- rest 8 [this is a rest with the duration of a 8th note]

The files `stratosphere_input.txt` and `stratosphere_output.txt` are the most comprehensive examples in the `examples` folder, and `stratosphere_input.txt` has comments explaining how it works. It's totally not a practical tune to use as your init, but it's didactic for sure.
