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














dustbin_random.py l y 10000
real	1m37.107s
user	0m12.355s
sys	0m21.973s

dustbin_random.py r n 10000
real	0m0.613s
user	0m0.306s
sys	0m0.067s


dustbin_random.py p n 10000 + attotree
real    27m14.170s
user    264m37.954s
sys     0m39.923s



p_bwt_lite :
[M::main] Real time: 23956.893 sec; CPU: 128792.791 sec; Peak RSS: 21.850 GB
125342.27user 3451.00system 6:39:20elapsed 537%CPU (0avgtext+0avgdata 22911608maxresident)k
82005608inputs+81225032outputs (6major+2190366421minor)pagefaults 0swaps

-rw-r--r-- 1 aantao cnrs_umr6074  39G 14 févr. 09:30 p.bwt

r_bwt_lite :
[M::main] Real time: 24357.076 sec; CPU: 143281.454 sec; Peak RSS: 22.103 GB
139341.59user 3939.91system 6:46:01elapsed 588%CPU (0avgtext+0avgdata 23176656maxresident)k
50419008inputs+81224584outputs (3major+2312173503minor)pagefaults 0swaps












l_bwt :
[M::main] Real time: 38707.264 sec; CPU: 302143.325 sec; Peak RSS: 37.051 GB
283988.01user 18155.70system 10:45:08elapsed 780%CPU (0avgtext+0avgdata 38850372maxresident)k
82010472inputs+162435344outputs (9major+7324113361minor)pagefaults 0swaps

l_bwt_lite :
[M::main] Real time: 24921.805 sec; CPU: 134801.198 sec; Peak RSS: 21.899 GB
130586.14user 4215.59system 6:55:24elapsed 540%CPU (0avgtext+0avgdata 22962988maxresident)k
81375040inputs+81224888outputs (4major+2481824332minor)pagefaults 0swaps


-rw-r--r-- 1 aantao cnrs_umr6074 78G 10 févr. 07:25 random_dustbin_l.bwt
-rw-r--r-- 1 aantao cnrs_umr6074 39G 10 févr. 06:57 random_dustbin_l_lite.bwt

plain2fmd l lite
[M::main] Real time: 375.820 sec; CPU: 347.353 sec; Peak RSS: 14.026 GB
real	6m16.086s
user	5m26.428s
sys	0m21.171s

-rw-r--r-- 1 aantao cnrs_umr6074 15G 10 févr. 12:25 bwt_l_lite.fmd

2797082 sequences
41576335807 symbols
14153759271 runs
9349939752 A
11419006816 C
11418963178 G
9385337779 T
291200 N

