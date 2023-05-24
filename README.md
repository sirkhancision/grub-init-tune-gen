## grub-init-tune-gen

This tool takes a manual input of notes and their duration and generates a code to be used in `GRUB_INIT_TUNE` at `/etc/default/grub`. The process can be quite long depending on the track. 

It doesn't support tuplets but you can work around that: say that you have a track that is comprised mostly of triplets, you can multiply the tempo times 3/2
- The grandma_nier.txt example in the `examples` folder is originally a track with 107 BPM and triplets, but the tempo provided was 161, because `ceiling(107 * (3/2)) = 161`
