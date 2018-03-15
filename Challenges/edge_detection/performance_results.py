import pstats

stats = pstats.Stats('edge_detection.profile')
stats.strip_dirs().sort_stats('time').print_stats()
