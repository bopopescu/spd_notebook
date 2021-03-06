from misc import (alarm, ellipsis_range, ellipsis_iter, srange, xsrange, sxrange, getitem,
                  cputime, verbose, set_verbose, set_verbose_files,
                  get_verbose_files, unset_verbose_files, get_verbose, 
                  version, banner, add, union, uniq, powerset, subsets,
                  exists, forall, 
                  random_sublist, mul, walltime, generic_cmp,
                  repr_lincomb, tmp_dir, tmp_filename,
                  pad_zeros, attrcall,
                  DOT_SAGE, SAGE_ROOT, SAGE_URL, SAGE_DB, SAGE_TMP,
                  newton_method_sizes,
                  is_64_bit, is_32_bit, prod, running_total)

from html import html

from sage_timeit_class import timeit

from edit_module import edit, set_edit_template

from flatten import flatten

from map_threaded import map_threaded

from session import load_session, save_session, show_identifiers

from remote_file import get_remote_file

from attach import attach

from profiler import Profiler

from mrange import xmrange, mrange, xmrange_iter, mrange_iter, cartesian_product_iterator

from fpickle import pickle_function, unpickle_function

# deprecated
#from bug import bug

from dist import install_scripts

# deprecated
#from darcs import darcs_src, darcs_doc, darcs_scripts

from hg import hg_sage, hg_scripts, hg_extcode

from package import install_package, is_package_installed, standard_packages, optional_packages, experimental_packages, upgrade

from pager import pager

from sagedoc import search_src, search_def, search_doc

from classgraph import class_graph

from reset import reset, restore

from getusage import top, get_memory_usage

from log import log_html, log_dvi, log_text

from mathml import mathml

from defaults import set_default_variable_name

from preparser import preparse, implicit_multiplication, BackslashOperator

from interpreter import preparser

from sage_eval import sage_eval, sageobj

from sage_input import sage_input

from cython import cython_lambda, cython_create_local_so
from cython_c import cython
pyrex = cython # synonym -- for now
sagex = cython # synonym -- for now

from persist import save, load, dumps, loads, db, db_save

from func_persist import func_persist

from functional import (additive_order,
                        sqrt as numerical_sqrt,
                        arg,
                        base_ring,
                        base_field,
                        basis,
                        category,
                        charpoly,
                        characteristic_polynomial,
                        coerce,
                        cyclotomic_polynomial,
                        decomposition,
                        denominator,
                        det,
                        dimension,
                        dim,
                        discriminant,
                        disc,
                        eta,
                        exp,
                        factor,
                        fcp,
                        gen,
                        gens,
                        hecke_operator,
                        ideal,
                        image,
                        imag,
                        imaginary,
                        integral,
                        integral_closure,
                        interval,
                        xinterval,
                        is_commutative,
                        is_even,
                        is_integrally_closed,
                        is_field,
                        is_odd,
                        kernel,
                        krull_dimension,
                        lift,
                        minimal_polynomial,
                        minpoly,
                        multiplicative_order,
                        ngens,
                        norm,
                        numerator,
                        numerical_approx,
                        n, N,
                        objgens,
                        objgen,
                        one,
                        order,
                        rank,
                        real,
                        regulator,
                        round,
                        quotient,
                        quo,
                        show,
                        isqrt,
                        squarefree_part,
                        transpose,
                        zero,
                        log as log_b,
                        parent)


from latex import latex, view, pretty_print, pretty_print_default
 
# disabled -- nobody uses mathml
#from mathml ml

from trace import trace

from cachefunc import CachedFunction, cached_function, cached_method

from lazy_attribute import lazy_attribute

from sagex_ds import BinaryTree

from randstate import seed, set_random_seed, initial_seed, current_randstate

from prandom import *

##########################################################################
def benchmark(n=-1):
    """
    Run a well-chosen range of Sage commands and record the time it
    takes for each to run.

    INPUT:
        n -- int (default: -1) the benchmark number; the default
             of -1 runs all the benchmarks.
    OUTPUT:
        list -- summary of timings for each benchmark.
    """
    import sage.misc.benchmark
    return sage.misc.benchmark.benchmark(n)


class logstr(str):
    def __repr__(self):
        return self
    
    def _latex_(self):
        #return "\\begin{verbatim}%s\\end{verbatim}"%self
        if not '#' in self:
         delim = '#'
        elif not '@' in self:
         delim = '@'
        elif not '~' in self:
         delim = '~'
        return r"""\verb%s%s%s"""%(delim, self.replace('\n\n','\n').replace('\n','; '), delim)

