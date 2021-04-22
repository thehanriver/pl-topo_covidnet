pl-topo_covidnet
================================

.. image:: https://img.shields.io/docker/v/fnndsc/pl-topo_covidnet?sort=semver
    :target: https://hub.docker.com/r/thehanriver/pl-topo_covidnet

.. image:: https://img.shields.io/github/license/fnndsc/pl-topo_covidnet
    :target: https://github.com/thehanriver/pl-topo_covidnet/blob/master/LICENSE

.. image:: https://github.com/FNNDSC/pl-topo_covidnet/workflows/ci/badge.svg
    :target: https://github.com/thehanriver/pl-topo_covidnet/actions


.. contents:: Table of Contents


Abstract
--------

An app to work with TS plugins for with COVIDNET


Description
-----------

``topo_covidnet`` is a ChRIS-based application that is a copy of covidnet that also puts output in a sub directory


Usage
-----

.. code::

    python topo_covidnet.py
        [-h|--help]
        [--json] [--man] [--meta]
        [--savejson <DIR>]
        [-v|--verbosity <level>]
        [--version]
        [--parInst]
        <inputDir> <outputDir>


Arguments
~~~~~~~~~

.. code::

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
    
    [--parInst]
    Takes in Parent Instance ID to make sub directory in output


Getting inline help is:

.. code:: bash

    docker run --rm fnndsc/pl-topo_covidnet topo_covidnet --man

Run
~~~

You need to specify input and output directories using the `-v` flag to `docker run`.


.. code:: bash

    docker run --rm -u $(id -u)                                         \
        -v $(pwd)/in:/incoming -v $(pwd)/out:/outgoing                  \
        fnndsc/pl-topo_covidnet topo_covidnet   --parInst <insert ID>   \
        /incoming /outgoing

.. code:: bash

    docker run --rm -v $PWD/in:/incoming -v $PWD/out:/outgoing    \
        fnndsc/pl-topo_covidnet topo_covidnet                         \
               --imagefile ex-covid.jpeg /incoming /outgoing

Development
-----------

Build the Docker container:

.. code:: bash

    docker build -t local/pl-topo_covidnet .

Run unit tests:

.. code:: bash

    docker run --rm local/pl-topo_covidnet nosetests

Examples
--------

Put some examples here!


.. image:: https://raw.githubusercontent.com/FNNDSC/cookiecutter-chrisapp/master/doc/assets/badge/light.png
    :target: https://chrisstore.co
