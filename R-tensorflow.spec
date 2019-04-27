#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-tensorflow
Version  : 1.13.1
Release  : 11
URL      : https://cran.r-project.org/src/contrib/tensorflow_1.13.1.tar.gz
Source0  : https://cran.r-project.org/src/contrib/tensorflow_1.13.1.tar.gz
Summary  : R Interface to 'TensorFlow'
Group    : Development/Tools
License  : Apache-2.0
Requires: R-Rcpp
Requires: R-base64enc
Requires: R-config
Requires: R-jsonlite
Requires: R-processx
Requires: R-reticulate
Requires: R-rstudioapi
Requires: R-tfruns
Requires: R-whisker
Requires: R-yaml
BuildRequires : R-Rcpp
BuildRequires : R-base64enc
BuildRequires : R-config
BuildRequires : R-jsonlite
BuildRequires : R-processx
BuildRequires : R-reticulate
BuildRequires : R-rstudioapi
BuildRequires : R-tfruns
BuildRequires : R-whisker
BuildRequires : R-yaml
BuildRequires : buildreq-R

%description
an open source software library for numerical computation using data
  flow graphs. Nodes in the graph represent mathematical operations, 
  while the graph edges represent the multidimensional data arrays 
  (tensors) communicated between them. The flexible architecture allows
  you to deploy computation to one or more 'CPUs' or 'GPUs' in a desktop, 
  server, or mobile device with a single 'API'. 'TensorFlow' was originally
  developed by researchers and engineers working on the Google Brain Team 
  within Google's Machine Intelligence research organization for the 
  purposes of conducting machine learning and deep neural networks research,
  but the system is general enough to be applicable in a wide variety
  of other domains as well.

%prep
%setup -q -c -n tensorflow

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1554472623

%install
export SOURCE_DATE_EPOCH=1554472623
rm -rf %{buildroot}
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library tensorflow
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library tensorflow
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library tensorflow
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc tensorflow || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/tensorflow/DESCRIPTION
/usr/lib64/R/library/tensorflow/INDEX
/usr/lib64/R/library/tensorflow/Meta/Rd.rds
/usr/lib64/R/library/tensorflow/Meta/features.rds
/usr/lib64/R/library/tensorflow/Meta/hsearch.rds
/usr/lib64/R/library/tensorflow/Meta/links.rds
/usr/lib64/R/library/tensorflow/Meta/nsInfo.rds
/usr/lib64/R/library/tensorflow/Meta/package.rds
/usr/lib64/R/library/tensorflow/NAMESPACE
/usr/lib64/R/library/tensorflow/NEWS.md
/usr/lib64/R/library/tensorflow/R/tensorflow
/usr/lib64/R/library/tensorflow/R/tensorflow.rdb
/usr/lib64/R/library/tensorflow/R/tensorflow.rdx
/usr/lib64/R/library/tensorflow/examples/config/flags.yml
/usr/lib64/R/library/tensorflow/examples/hello.R
/usr/lib64/R/library/tensorflow/examples/introduction.R
/usr/lib64/R/library/tensorflow/examples/mnist/fully_connected_feed.R
/usr/lib64/R/library/tensorflow/examples/mnist/mnist.R
/usr/lib64/R/library/tensorflow/examples/mnist/mnist_softmax.R
/usr/lib64/R/library/tensorflow/examples/mnist/mnist_with_summaries.R
/usr/lib64/R/library/tensorflow/examples/regression/tensorflow_linear_regression.R
/usr/lib64/R/library/tensorflow/help/AnIndex
/usr/lib64/R/library/tensorflow/help/aliases.rds
/usr/lib64/R/library/tensorflow/help/paths.rds
/usr/lib64/R/library/tensorflow/help/tensorflow.rdb
/usr/lib64/R/library/tensorflow/help/tensorflow.rdx
/usr/lib64/R/library/tensorflow/html/00Index.html
/usr/lib64/R/library/tensorflow/html/R.css
/usr/lib64/R/library/tensorflow/tests/testthat.R
/usr/lib64/R/library/tensorflow/tests/testthat/test-arguments.R
/usr/lib64/R/library/tensorflow/tests/testthat/test-examples.R
/usr/lib64/R/library/tensorflow/tests/testthat/test-export-savedmodel.R
/usr/lib64/R/library/tensorflow/tests/testthat/test-extract-syntax.R
/usr/lib64/R/library/tensorflow/tests/testthat/test-generic-methods.R
/usr/lib64/R/library/tensorflow/tests/testthat/utils.R
