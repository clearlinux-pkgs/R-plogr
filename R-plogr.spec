#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-plogr
Version  : 0.2.0
Release  : 50
URL      : https://cran.r-project.org/src/contrib/plogr_0.2.0.tar.gz
Source0  : https://cran.r-project.org/src/contrib/plogr_0.2.0.tar.gz
Summary  : The 'plog' C++ Logging Library
Group    : Development/Tools
License  : MIT
BuildRequires : buildreq-R

%description
A simple header-only logging library for C++.

%prep
%setup -q -c -n plogr
cd %{_builddir}/plogr

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1641075510

%install
export SOURCE_DATE_EPOCH=1641075510
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library plogr
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -ftree-vectorize -mno-vzeroupper  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library plogr
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library plogr
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc plogr || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/plogr/DESCRIPTION
/usr/lib64/R/library/plogr/INDEX
/usr/lib64/R/library/plogr/LICENSE
/usr/lib64/R/library/plogr/Meta/Rd.rds
/usr/lib64/R/library/plogr/Meta/features.rds
/usr/lib64/R/library/plogr/Meta/hsearch.rds
/usr/lib64/R/library/plogr/Meta/links.rds
/usr/lib64/R/library/plogr/Meta/nsInfo.rds
/usr/lib64/R/library/plogr/Meta/package.rds
/usr/lib64/R/library/plogr/NAMESPACE
/usr/lib64/R/library/plogr/NEWS.md
/usr/lib64/R/library/plogr/R/plogr
/usr/lib64/R/library/plogr/R/plogr.rdb
/usr/lib64/R/library/plogr/R/plogr.rdx
/usr/lib64/R/library/plogr/help/AnIndex
/usr/lib64/R/library/plogr/help/aliases.rds
/usr/lib64/R/library/plogr/help/paths.rds
/usr/lib64/R/library/plogr/help/plogr.rdb
/usr/lib64/R/library/plogr/help/plogr.rdx
/usr/lib64/R/library/plogr/html/00Index.html
/usr/lib64/R/library/plogr/html/R.css
/usr/lib64/R/library/plogr/include/plog/Appenders/ColorConsoleAppender.h
/usr/lib64/R/library/plogr/include/plog/Appenders/ConsoleAppender.h
/usr/lib64/R/library/plogr/include/plog/Appenders/IAppender.h
/usr/lib64/R/library/plogr/include/plog/Formatters/FuncMessageFormatter.h
/usr/lib64/R/library/plogr/include/plog/Init.h
/usr/lib64/R/library/plogr/include/plog/Log.h
/usr/lib64/R/library/plogr/include/plog/Logger.h
/usr/lib64/R/library/plogr/include/plog/Record.h
/usr/lib64/R/library/plogr/include/plog/Severity.h
/usr/lib64/R/library/plogr/include/plog/Util.h
/usr/lib64/R/library/plogr/include/plogr.h
