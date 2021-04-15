#
# topo_covidnet ds ChRIS plugin app
#
# (c) 2021 Fetal-Neonatal Neuroimaging & Developmental Science Center
#                   Boston Children's Hospital
#
#              http://childrenshospital.org/FNNDSC/
#                        dev@babyMRI.org
#

from chrisapp.base import ChrisApp
import os
import sys
from .inference import Inference

Gstr_title = """
 _                                   _     _            _   
| |                                 (_)   | |          | |  
| |_ ___  _ __   ___   ___ _____   ___  __| |_ __   ___| |_ 
| __/ _ \| '_ \ / _ \ / __/ _ \ \ / / |/ _` | '_ \ / _ \ __|
| || (_) | |_) | (_) | (_| (_) \ V /| | (_| | | | |  __/ |_ 
 \__\___/| .__/ \___/ \___\___/ \_/ |_|\__,_|_| |_|\___|\__|
         | |      ______                                    
         |_|     |______|                                   
"""

Gstr_synopsis = """

(Edit this in-line help for app specifics. At a minimum, the 
flags below are supported -- in the case of DS apps, both
positional arguments <inputDir> and <outputDir>; for FS and TS apps
only <outputDir> -- and similarly for <in> <out> directories
where necessary.)

    NAME

       topo_covidnet.py 

    SYNOPSIS

        python topo_covidnet.py                                         \\
            [-h] [--help]                                               \\
            [--json]                                                    \\
            [--man]                                                     \\
            [--meta]                                                    \\
            [--savejson <DIR>]                                          \\
            [-v <level>] [--verbosity <level>]                          \\
            [--version]                                                 \\
            <inputDir>                                                  \\
            <outputDir> 

    BRIEF EXAMPLE

        * Bare bones execution

            docker run --rm -u $(id -u)                             \
                -v $(pwd)/in:/incoming -v $(pwd)/out:/outgoing      \
                fnndsc/pl-topo_covidnet topo_covidnet                        \
                /incoming /outgoing

    DESCRIPTION

        `topo_covidnet.py` ...

    ARGS

        [-h] [--help]
        If specified, show help message and exit.
        
        [--json]
        If specified, show json representation of app and exit.
        
        [--man]
        If specified, print (this) man page and exit.

        [--meta]
        If specified, print plugin meta data and exit.
        
        [--savejson <DIR>] 
        If specified, save json representation file to DIR and exit. 
        
        [-v <level>] [--verbosity <level>]
        Verbosity level for app. Not used currently.
        
        [--version]
        If specified, print version number and exit. 
"""


class Topo_covidnet(ChrisApp):
    """
    An app to work with TS plugins
    """
    PACKAGE                 = __package__
    TITLE                   = 'A copy of COVIDNET to work on TS plugins'
    CATEGORY                = ''
    TYPE                    = 'ds'
    ICON                    = ''   # url of an icon image
    MIN_NUMBER_OF_WORKERS   = 1    # Override with the minimum number of workers as int
    MAX_NUMBER_OF_WORKERS   = 1    # Override with the maximum number of workers as int
    MIN_CPU_LIMIT           = 1000 # Override with millicore value as int (1000 millicores == 1 CPU core)
    MIN_MEMORY_LIMIT        = 200  # Override with memory MegaByte (MB) limit as int
    MIN_GPU_LIMIT           = 0    # Override with the minimum number of GPUs as int
    MAX_GPU_LIMIT           = 0    # Override with the maximum number of GPUs as int
    OUTPUT_META_DICT = {}

    def define_parameters(self):
        """
        Arguments accepted by plugin
        """
        self.add_argument('--parInst',
        	dest      = 'parInst',
        	type      = str,
        	optional  = False,
        	help      = 'Parent instance ID',)
        self.add_argument('--metaname', 
                    dest         = 'metaname', 
                    type         = str, 
                    optional     = True,
                    help         = 'Name of ckpt meta file',
                    default      = 'model.meta')
        self.add_argument('--imagefile', 
                    dest         = 'imagefile', 
                    type         = str, 
                    optional     = False,
                    help         = 'Name of image file to infer from')
        self.add_argument('--in_tensorname', 
                    dest         = 'in_tensorname', 
                    type         = str, 
                    optional     = True,
                    help         = 'Name of input tensor to graph',
                    default      = 'input_1:0')
        self.add_argument('--out_tensorname', 
                    dest         = 'out_tensorname', 
                    type         = str, 
                    optional     = True,
                    help         = 'Name of output tensor from graph',
                    default      = 'norm_dense_1/Softmax:0')
        self.add_argument('--input_size', 
                    dest         = 'input_size', 
                    type         = int, 
                    optional     = True,
                    help         = 'Size of input (ex: if 480x480, --input_size 480)',
                    default      = 480)
        self.add_argument('--top_percent', 
                    dest         = 'top_percent', 
                    type         = float, 
                    optional     = True,
                    help         = 'Percent top crop from top of image',
                    default      = 0.08)

    def run(self, options):
        """
        Define the code to be run by this plugin app.
        """
        print(Gstr_title)
        print('Version: %s' % self.get_version())
        all_three_models = [
            # {
            #     'weightspath':'/models/COVIDNet-CXR3-A',
            #     'ckptname':'model-2856',
            #     'modelused':'modelA'
            # }, 
            {
                'weightspath':'/usr/local/lib/covidnet/COVIDNet-CXR4-B',
                'ckptname':'model-1545',
                'modelused':'modelB'
            },
            # {
            #     'weightspath': '/models/COVIDNet-CXR3-C',
            #     'ckptname':'model-0',
            #     'modelused':'modelC'
            # }
        ]
        for model in all_three_models:
            options.weightspath =model['weightspath']
            options.ckptname = model['ckptname']
            options.modelused = model['modelused']
            infer_obj = Inference(options)
            infer_obj.infer()

    def show_man_page(self):
        """
        Print the app's man page.
        """
        print(Gstr_synopsis)
