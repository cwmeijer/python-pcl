"""
Run the registration algorithm on PCD or ply files files.
"""

import argparse
import pcl
import pcl.registration

def parse_args():
    """ Parse arguments from the command-line using argparse """
    parser = argparse.ArgumentParser(description='Registration for two PLY point clouds')
    parser.add_argument('-f','--function', help='Registration algorithm to run. Choose between gicp, icp, icp_nl, and ia_ransac. Defaults to gicp')
    parser.add_argument('source', metavar="SOURCE", help="Source PLY/PCD file")
    parser.add_argument('target', metavar="TARGET", help="Target PLY/PCD file to map source to")
    return parser.parse_args()

def process_args(args):
    """ Read source, target and algorithm """
    print "Reading source", args.source
    source = pcl.load(args.source)
    print "Reading target ", args.target
    target = pcl.load(args.target)
    
    funcs = {
        'icp': pcl.registration.icp,
        'gicp': pcl.registration.gicp,
        'icp_nl': pcl.registration.icp_nl,
        'ia_ransac': pcl.registration.ia_ransac
    }
    
    if args.function in funcs:
        algo = funcs[args.function]
    else:
        algo = pcl.registration.gicp
    
    return source, target, algo

def run_algo(algorithm, source, target, **kwargs):
    

def print_output(algo, converged, transf, fitness):
    """ Print some output based on the algorithm output """
    
    print "------", algo.__name__, "-----"
    print "Converged: ", converged, "Fitness: ", fitness
    print "Rotation: "
    print transf[0:3,0:3]
    print "Translation: ", transf[3, 0:3]
    print "---------------"

if __name__ == '__main__':
    args = parse_args()
    source, target, algo = process_args(args)
    converged, transf, estimate, fitness = algo(source, target)
    print_output(algo, converged, transf, fitness)