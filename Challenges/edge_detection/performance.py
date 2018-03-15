import cProfile
import edge_detection

image = '7 15 4 100 15 25 2 175 2 25 5 175 2 25 5'
result = '7 85 5 0 2 85 5 75 10 150 2 75 3 0 2 150 2 0 4'

cProfile.run('edge_detection.edge_detection(image)', 'edge_detection.profile')
