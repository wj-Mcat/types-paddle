from __future__ import annotations
from typing import Optional

class Tensor:
    def abs(self, name: Optional[str] = None): ...
    def acos(self, name: Optional[str] = None): ...
    def acosh(self, name: Optional[str] = None): ...
    def add(self, y: Tensor, name: Optional[str] = None): ...
    def add_(self, y: Tensor, name: Optional[str] = None): ...
    def add_n(self, name: Optional[str] = None): ...
    def addmm(self, x, y, beta=1.0, alpha=1.0, name: Optional[str] = None): ...
    def all(self, axis: Optional[int] = None, keepdim: bool = False, name: Optional[str] = None): ...
    def allclose(self, y: Tensor, rtol=1e-05, atol=1e-08, equal_nan=False, name: Optional[str] = None): ...
    def amax(self, axis: Optional[int] = None, keepdim: bool = False, name: Optional[str] = None): ...
    def amin(self, axis: Optional[int] = None, keepdim: bool = False, name: Optional[str] = None): ...
    def angle(self, name: Optional[str] = None): ...
    def any(self, axis: Optional[int] = None, keepdim: bool = False, name: Optional[str] = None): ...
    def argmax(self, axis: Optional[int] = None, keepdim: bool = False, dtype='int64', name: Optional[str] = None): ...
    def argmin(self, axis: Optional[int] = None, keepdim: bool = False, dtype='int64', name: Optional[str] = None): ...
    def argsort(self, axis: int = -1, descending=False, name: Optional[str] = None): ...
    def as_complex(self, name: Optional[str] = None): ...
    def as_real(self, name: Optional[str] = None): ...
    def asin(self, name: Optional[str] = None): ...
    def asinh(self, name: Optional[str] = None): ...
    def astype(self, dtype): ...
    def atan(self, name: Optional[str] = None): ...
    def atanh(self, name: Optional[str] = None): ...
    def backward(self, grad_tensor=None, retain_graph=False): ...
    def bincount(self, weights=None, minlength=0, name: Optional[str] = None): ...
    def bitwise_and(self, y: Tensor, out=None, name: Optional[str] = None): ...
    def bitwise_not(self, out=None, name: Optional[str] = None): ...
    def bitwise_or(self, y: Tensor, out=None, name: Optional[str] = None): ...
    def bitwise_xor(self, y: Tensor, out=None, name: Optional[str] = None): ...
    def bmm(self, y: Tensor, name: Optional[str] = None): ...
    def broadcast_shape(self, y_shape): ...
    def broadcast_tensors(self, name: Optional[str] = None): ...
    def broadcast_to(self, shape, name: Optional[str] = None): ...
    def cast(self, dtype): ...
    def ceil(self, name: Optional[str] = None): ...
    def ceil_(self, name: Optional[str] = None): ...
    def cholesky(self, upper=False, name: Optional[str] = None): ...
    def cholesky_solve(self, y: Tensor, upper=False, name: Optional[str] = None): ...
    def chunk(self, chunks, axis: int = 0, name: Optional[str] = None): ...
    def clear_grad(self): ...
    def clip(self, min=None, max=None, name: Optional[str] = None): ...
    def clip_(self, min=None, max=None, name: Optional[str] = None): ...
    def concat(self, axis: int = 0, name: Optional[str] = None): ...
    def cond(self, p=None, name: Optional[str] = None): ...
    def conj(self, name: Optional[str] = None): ...
    def cos(self, name: Optional[str] = None): ...
    def cosh(self, name: Optional[str] = None): ...
    def cov(self, rowvar=True, ddof=True, fweights=None, aweights=None, name: Optional[str] = None): ...
    def cross(self, y: Tensor, axis: int = 9, name: Optional[str] = None): ...
    def cumprod(self, dim=None, dtype=None, name: Optional[str] = None): ...
    def cumsum(self, axis: Optional[int] = None, dtype=None, name: Optional[str] = None): ...
    def deg2rad(self, name: Optional[str] = None): ...
    def diagonal(self, offset=0, axis1=0, axis2=1, name: Optional[str] = None): ...
    def diff(self, n=1, axis: int = -1, prepend=None, append=None, name: Optional[str] = None): ...
    def digamma(self, name: Optional[str] = None): ...
    def dim(self): ...
    def dist(self, y: Tensor, p=2, name: Optional[str] = None): ...
    def divide(self, y: Tensor, name: Optional[str] = None): ...
    def dot(self, y: Tensor, name: Optional[str] = None): ...
    def eig(self, name: Optional[str] = None): ...
    def eigvals(self, name: Optional[str] = None): ...
    def eigvalsh(self, UPLO='L', name: Optional[str] = None): ...
    def equal(self, y: Tensor, name: Optional[str] = None): ...
    def equal_all(self, y: Tensor, name: Optional[str] = None): ...
    def erf(self, name: Optional[str] = None): ...
    def erfinv(self, name: Optional[str] = None): ...
    def erfinv_(self, name: Optional[str] = None): ...
    def exp(self, name: Optional[str] = None): ...
    def exp_(self, name: Optional[str] = None): ...
    def expand(self, shape, name: Optional[str] = None): ...
    def expand_as(self, y: Tensor, name: Optional[str] = None): ...
    def exponential_(self, lam=1.0, name: Optional[str] = None): ...
    def fill_(self, value): ...
    def fill_diagonal_(self, value, offset=0, wrap=False, name: Optional[str] = None): ...
    def fill_diagonal_tensor(self, y: Tensor, offset=0, dim1=0, dim2=1, name: Optional[str] = None): ...
    def fill_diagonal_tensor_(self, y: Tensor, offset=0, dim1=0, dim2=1, name: Optional[str] = None): ...
    def flatten(self, start_axis: int = 0, stop_axis: int = -1, name: Optional[str] = None): ...
    def flatten_(self, start_axis: int = 0, stop_axis: int = -1, name: Optional[str] = None): ...
    def flip(self, axis, name: Optional[str] = None): ...
    def floor(self, name: Optional[str] = None): ...
    def floor_(self, name: Optional[str] = None): ...
    def floor_divide(self, y: Tensor, name: Optional[str] = None): ...
    def floor_mod(self, y: Tensor, name: Optional[str] = None): ...
    def fmax(self, y: Tensor, name: Optional[str] = None): ...
    def fmin(self, y: Tensor, name: Optional[str] = None): ...
    def gather(self, index, axis: Optional[int] = None, name: Optional[str] = None): ...
    def gather_nd(self, index, name: Optional[str] = None): ...
    def gcd(self, y: Tensor, name: Optional[str] = None): ...
    def gradient(self): ...
    def greater_equal(self, y: Tensor, name: Optional[str] = None): ...
    def greater_than(self, y: Tensor, name: Optional[str] = None): ...
    def histogram(self, bins=100, min=0, max=0, name: Optional[str] = None): ...
    def imag(self, name: Optional[str] = None): ...
    def increment(self, value=1.0, name: Optional[str] = None): ...
    def index_sample(self, index): ...
    def index_select(self, index, axis: int = 0, name: Optional[str] = None): ...
    def inner(self, y: Tensor, name: Optional[str] = None): ...
    def inverse(self, name: Optional[str] = None): ...
    def is_complex(self): ...
    def is_empty(self, name: Optional[str] = None): ...
    def is_floating_point(self): ...
    def is_integer(self): ...
    def is_tensor(self): ...
    def isclose(self, y: Tensor, rtol=1e-05, atol=1e-08, equal_nan=False, name: Optional[str] = None): ...
    def isfinite(self, name: Optional[str] = None): ...
    def isinf(self, name: Optional[str] = None): ...
    def isnan(self, name: Optional[str] = None): ...
    def item(self, *args): ...
    def kron(self, y: Tensor, name: Optional[str] = None): ...
    def kthvalue(self, k, axis: Optional[int] = None, keepdim: bool = False, name: Optional[str] = None): ...
    def lcm(self, y: Tensor, name: Optional[str] = None): ...
    def lerp(self, y: Tensor, weight, name: Optional[str] = None): ...
    def lerp_(self, y: Tensor, weight, name: Optional[str] = None): ...
    def less_equal(self, y: Tensor, name: Optional[str] = None): ...
    def less_than(self, y: Tensor, name: Optional[str] = None): ...
    def lgamma(self, name: Optional[str] = None): ...
    def log(self, name: Optional[str] = None): ...
    def log10(self, name: Optional[str] = None): ...
    def log1p(self, name: Optional[str] = None): ...
    def log2(self, name: Optional[str] = None): ...
    def logical_and(self, y: Tensor, out=None, name: Optional[str] = None): ...
    def logical_not(self, out=None, name: Optional[str] = None): ...
    def logical_or(self, y: Tensor, out=None, name: Optional[str] = None): ...
    def logical_xor(self, y: Tensor, out=None, name: Optional[str] = None): ...
    def logit(self, eps=None, name: Optional[str] = None): ...
    def logsumexp(self, axis: Optional[int] = None, keepdim: bool = False, name: Optional[str] = None): ...
    def lstsq(self, y: Tensor, rcond=None, driver=None, name: Optional[str] = None): ...
    def lu(self, pivot=True, get_infos=False, name: Optional[str] = None): ...
    def lu_unpack(self, y: Tensor, unpack_ludata=True, unpack_pivots=True, name: Optional[str] = None): ...
    def masked_select(self, mask, name: Optional[str] = None): ...
    def matmul(self, y: Tensor, transpose_x=False, transpose_y=False, name: Optional[str] = None): ...
    def matrix_power(self, n, name: Optional[str] = None): ...
    def max(self, axis: Optional[int] = None, keepdim: bool = False, name: Optional[str] = None): ...
    def maximum(self, y: Tensor, name: Optional[str] = None): ...
    def mean(self, axis: Optional[int] = None, keepdim: bool = False, name: Optional[str] = None): ...
    def median(self, axis: Optional[int] = None, keepdim: bool = False, name: Optional[str] = None): ...
    def min(self, axis: Optional[int] = None, keepdim: bool = False, name: Optional[str] = None): ...
    def minimum(self, y: Tensor, name: Optional[str] = None): ...
    def mm(self, mat2, name: Optional[str] = None): ...
    def mod(self, y: Tensor, name: Optional[str] = None): ...
    def mode(self, axis: int = -1, keepdim: bool = False, name: Optional[str] = None): ...
    def moveaxis(self, source, destination, name: Optional[str] = None): ...
    def multi_dot(self, name: Optional[str] = None): ...
    def multiplex(self, index, name: Optional[str] = None): ...
    def multiply(self, y: Tensor, name: Optional[str] = None): ...
    def mv(self, vec, name: Optional[str] = None): ...
    def nanmean(self, axis: Optional[int] = None, keepdim: bool = False, name: Optional[str] = None): ...
    def nansum(self, axis: Optional[int] = None, dtype=None, keepdim: bool = False, name: Optional[str] = None): ...
    def ndimension(self): ...
    def neg(self, name: Optional[str] = None): ...
    def nonzero(self, as_tuple=False): ...
    def norm(self, p='fro', axis: Optional[int] = None, keepdim: bool = False, name: Optional[str] = None): ...
    def not_equal(self, y: Tensor, name: Optional[str] = None): ...
    def numel(self, name: Optional[str] = None): ...
    def outer(self, y: Tensor, name: Optional[str] = None): ...
    def pow(self, y: Tensor, name: Optional[str] = None): ...
    def prod(self, axis: Optional[int] = None, keepdim: bool = False, dtype=None, name: Optional[str] = None): ...
    def put_along_axis(self, indices, values, axis, reduce='assign'): ...
    def put_along_axis_(self, indices, values, axis, reduce='assign'): ...
    def qr(self, mode='reduced', name: Optional[str] = None): ...
    def quantile(self, q, axis: Optional[int] = None, keepdim: bool = False): ...
    def rad2deg(self, name: Optional[str] = None): ...
    def rank(self): ...
    def real(self, name: Optional[str] = None): ...
    def reciprocal(self, name: Optional[str] = None): ...
    def reciprocal_(self, name: Optional[str] = None): ...
    def register_hook(self, hook): ...
    def remainder(self, y: Tensor, name: Optional[str] = None): ...
    def repeat_interleave(self, repeats, axis: Optional[int] = None, name: Optional[str] = None): ...
    def reshape(self, shape, name: Optional[str] = None): ...
    def reshape_(self, shape, name: Optional[str] = None): ...
    def reverse(self, axis, name: Optional[str] = None): ...
    def roll(self, shifts, axis: Optional[int] = None, name: Optional[str] = None): ...
    def rot90(self, k=1, axes=[0, 1], name: Optional[str] = None): ...
    def round(self, name: Optional[str] = None): ...
    def round_(self, name: Optional[str] = None): ...
    def rsqrt(self, name: Optional[str] = None): ...
    def rsqrt_(self, name: Optional[str] = None): ...
    def scale(self, scale=1.0, bias=0.0, bias_after_scale=True, act=None, name: Optional[str] = None): ...
    def scale_(self, scale=1.0, bias=0.0, bias_after_scale=True, act=None, name: Optional[str] = None): ...
    def scatter(self, index, updates, overwrite=True, name: Optional[str] = None): ...
    def scatter_(self, index, updates, overwrite=True, name: Optional[str] = None): ...
    def scatter_nd(self, updates, shape, name: Optional[str] = None): ...
    def scatter_nd_add(self, index, updates, name: Optional[str] = None): ...
    def set_value(self, value): ...
    def shard_index(self, index_num, nshards, shard_id, ignore_value=-1): ...
    def sign(self, name: Optional[str] = None): ...
    def sin(self, name: Optional[str] = None): ...
    def sinh(self, name: Optional[str] = None): ...
    def slice(self, axes, starts, ends): ...
    def solve(self, y: Tensor, name: Optional[str] = None): ...
    def sort(self, axis: int = -1, descending=False, name: Optional[str] = None): ...
    def split(self, num_or_sections, axis: int = 0, name: Optional[str] = None): ...
    def sqrt(self, name: Optional[str] = None): ...
    def sqrt_(self, name: Optional[str] = None): ...
    def square(self, name: Optional[str] = None): ...
    def squeeze(self, axis: Optional[int] = None, name: Optional[str] = None): ...
    def squeeze_(self, axis: Optional[int] = None, name: Optional[str] = None): ...
    def stack(self, axis: int = 0, name: Optional[str] = None): ...
    def stanh(self, scale_a=0.67, scale_b=1.7159, name: Optional[str] = None): ...
    def std(self, axis: Optional[int] = None, unbiased=True, keepdim: bool = False, name: Optional[str] = None): ...
    def strided_slice(self, axes, starts, ends, strides, name: Optional[str] = None): ...
    def subtract(self, y: Tensor, name: Optional[str] = None): ...
    def subtract_(self, y: Tensor, name: Optional[str] = None): ...
    def sum(self, axis: Optional[int] = None, dtype=None, keepdim: bool = False, name: Optional[str] = None): ...
    def t(self, name: Optional[str] = None): ...
    def take_along_axis(self, indices, axis): ...
    def tanh(self, name: Optional[str] = None): ...
    def tanh_(self, name: Optional[str] = None): ...
    def tensordot(self, y: Tensor, axes=2, name: Optional[str] = None): ...
    def tile(self, repeat_times, name: Optional[str] = None): ...
    def to_dense(self): ...
    def to_sparse_coo(self, sparse_dim): ...
    def tolist(self): ...
    def topk(self, k, axis: Optional[int] = None, largest=True, sorted=True, name: Optional[str] = None): ...
    def trace(self, offset=0, axis1=0, axis2=1, name: Optional[str] = None): ...
    def transpose(self, perm, name: Optional[str] = None): ...
    def trunc(self, name: Optional[str] = None): ...
    def unbind(self, axis: int = 0): ...
    def uniform_(self, min=-1.0, max=1.0, seed=0, name: Optional[str] = None): ...
    def unique(self, return_index=False, return_inverse=False, return_counts=False, axis: Optional[int] = None, dtype='int64', name: Optional[str] = None): ...
    def unique_consecutive(self, return_inverse=False, return_counts=False, axis: Optional[int] = None, dtype='int64', name: Optional[str] = None): ...
    def unsqueeze(self, axis, name: Optional[str] = None): ...
    def unsqueeze_(self, axis, name: Optional[str] = None): ...
    def unstack(self, axis: int = 0, num=None): ...
    def values(self): ...
    def var(self, axis: Optional[int] = None, unbiased=True, keepdim: bool = False, name: Optional[str] = None): ...
    def where(self, x=None, y=None, name: Optional[str] = None): ...
    def zero_(self): ...
