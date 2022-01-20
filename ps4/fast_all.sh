# paternal vs. paternal
(time python dnaseq.py data/fpaternal0.fa data/fpaternal0.fa output/pat_pat_fast.png) &> output/pat_pat_fast.txt
# paternal vs. maternal
(time python dnaseq.py data/fpaternal0.fa data/fmaternal0.fa output/pat_mat_fast.png) &> output/pat_mat_fast.txt
# paternal vs. chimp
(time python dnaseq.py data/fpaternal0.fa data/fchimp0.fa output/pat_chimp_fast.png) &> output/pat_chimp_fast.txt
# paternal vs. dog
(time python dnaseq.py data/fpaternal0.fa data/fdog0.fa output/pat_dog_fast.png) &> output/pat_dog_fast.txt
# paternal vs. mouse
(time python dnaseq.py data/fpaternal0.fa data/fmouse0.fa output/pat_mouse_fast.png) &> output/pat_mouse_fast.txt
# dog vs. mouse
(time python dnaseq.py data/fdog0.fa data/fmouse0.fa output/dog_mouse_fast.png) &> output/dog_mouse_fast.txt