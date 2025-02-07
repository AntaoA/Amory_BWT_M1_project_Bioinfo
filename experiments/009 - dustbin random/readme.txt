We consider all dusbin batches.
We choose randomly 8k genomes.
We run the same thing as in 007 experiment (comparison between random, lexicographic and phylogenetic order)


1 - Select genome
2 - Attotree
3 - Make command for each order
4 - Run command
5 - Analyse BWT result




python dustbin_random.py [ordre] [new_selection?]
$(cat command_[order].txt)
ropebwt3 stat random_dustbin_[order].fmr



lexicographic
[M::mr_restore] ($, A, C, G, T, N) = (533853, 930398753, 1159208469, 1159004584, 932931451, 32830462)
533853 sequences
4214907572 symbols
2351049305 runs
930398753 A
1159208469 C
1159004584 G
932931451 T
32830462 N
[M::main] Version: 3.7-r226
[M::main] CMD: ropebwt3 stat random_dustbin.fmr
[M::main] Real time: 9.758 sec; CPU: 9.757 sec; Peak RSS: 3.891 GB

run length: 1.79


phylogenetic
[M::mr_restore] ($, A, C, G, T, N) = (533852, 930397518, 1159208469, 1159004584, 932930451, 32789630)
533852 sequences
4214864504 symbols
2351040426 runs
930397518 A
1159208469 C
1159004584 G
932930451 T
32789630 N
[M::main] Version: 3.7-r226
[M::main] CMD: ropebwt3 stat random_dustbin_p.fmr
[M::main] Real time: 6.230 sec; CPU: 6.228 sec; Peak RSS: 3.897 GB

run length: 1.79

random
[M::mr_restore] ($, A, C, G, T, N) = (533853, 930398753, 1159208469, 1159004584, 932931451, 32830462)
533853 sequences
4214907572 symbols
2351067068 runs
930398753 A
1159208469 C
1159004584 G
932931451 T
32830462 N
[M::main] Version: 3.7-r226
[M::main] CMD: ropebwt3 stat random_dustbin_r.fmr
[M::main] Real time: 7.251 sec; CPU: 7.251 sec; Peak RSS: 3.909 GB

run length: 1.79