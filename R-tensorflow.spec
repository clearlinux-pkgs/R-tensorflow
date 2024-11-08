#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: R
# autospec version: v10
# autospec commit: 5905be9
#
Name     : R-tensorflow
Version  : 2.16.0
Release  : 55
URL      : https://cran.r-project.org/src/contrib/tensorflow_2.16.0.tar.gz
Source0  : https://cran.r-project.org/src/contrib/tensorflow_2.16.0.tar.gz
Summary  : R Interface to 'TensorFlow'
Group    : Development/Tools
License  : Apache-2.0
Requires: R-config
Requires: R-lifecycle
Requires: R-processx
Requires: R-reticulate
Requires: R-rstudioapi
Requires: R-tfautograph
Requires: R-tfruns
Requires: R-yaml
BuildRequires : R-config
BuildRequires : R-lifecycle
BuildRequires : R-processx
BuildRequires : R-reticulate
BuildRequires : R-rstudioapi
BuildRequires : R-tfautograph
BuildRequires : R-tfruns
BuildRequires : R-yaml
BuildRequires : buildreq-R
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

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
%setup -q -n tensorflow
pushd ..
cp -a tensorflow buildavx2
popd
pushd ..
cp -a tensorflow buildavx512
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1713372323

%install
export SOURCE_DATE_EPOCH=1713372323
rm -rf %{buildroot}
LANG=C.UTF-8
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -flto -fno-semantic-interposition "
FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -flto -fno-semantic-interposition "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -flto -fno-semantic-interposition "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -flto -fno-semantic-interposition "
AR=gcc-ar
RANLIB=gcc-ranlib
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library
mkdir -p %{buildroot}-v3/usr/lib64/R/library
mkdir -p %{buildroot}-v4/usr/lib64/R/library
mkdir -p %{buildroot}-va/usr/lib64/R/library

mkdir -p ~/.R
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL  --install-tests --use-LTO --built-timestamp=${SOURCE_DATE_EPOCH} --data-compress=none --compress=none --build  -l %{buildroot}-v3/usr/lib64/R/library .
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --preclean  --install-tests --use-LTO --no-test-load --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}-v4/usr/lib64/R/library .
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean  --use-LTO --install-tests --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc . || :

/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}
/usr/bin/elf-move.py avx512 %{buildroot}-v4 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

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
/usr/lib64/R/library/tensorflow/help/AnIndex
/usr/lib64/R/library/tensorflow/help/aliases.rds
/usr/lib64/R/library/tensorflow/help/figures/lifecycle-archived.svg
/usr/lib64/R/library/tensorflow/help/figures/lifecycle-defunct.svg
/usr/lib64/R/library/tensorflow/help/figures/lifecycle-deprecated.svg
/usr/lib64/R/library/tensorflow/help/figures/lifecycle-experimental.svg
/usr/lib64/R/library/tensorflow/help/figures/lifecycle-maturing.svg
/usr/lib64/R/library/tensorflow/help/figures/lifecycle-questioning.svg
/usr/lib64/R/library/tensorflow/help/figures/lifecycle-soft-deprecated.svg
/usr/lib64/R/library/tensorflow/help/figures/lifecycle-stable.svg
/usr/lib64/R/library/tensorflow/help/figures/lifecycle-superseded.svg
/usr/lib64/R/library/tensorflow/help/paths.rds
/usr/lib64/R/library/tensorflow/help/tensorflow.rdb
/usr/lib64/R/library/tensorflow/help/tensorflow.rdx
/usr/lib64/R/library/tensorflow/html/00Index.html
/usr/lib64/R/library/tensorflow/html/R.css
/usr/lib64/R/library/tensorflow/tests/testthat.R
/usr/lib64/R/library/tensorflow/tests/testthat/helper-utils.R
/usr/lib64/R/library/tensorflow/tests/testthat/setup.R
/usr/lib64/R/library/tensorflow/tests/testthat/test-arguments.R
/usr/lib64/R/library/tensorflow/tests/testthat/test-as_tensor.R
/usr/lib64/R/library/tensorflow/tests/testthat/test-data-structures.R
/usr/lib64/R/library/tensorflow/tests/testthat/test-examples.R
/usr/lib64/R/library/tensorflow/tests/testthat/test-export-savedmodel.R
/usr/lib64/R/library/tensorflow/tests/testthat/test-extract-syntax.R
/usr/lib64/R/library/tensorflow/tests/testthat/test-generic-methods.R
/usr/lib64/R/library/tensorflow/tests/testthat/test-seed.R
/usr/lib64/R/library/tensorflow/tests/testthat/test-shape.R
/usr/lib64/R/library/tensorflow/tests/testthat/test-types.R
