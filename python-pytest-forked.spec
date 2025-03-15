#
# Conditional build:
%bcond_without	tests	# unit tests

Summary:	Run each test in a forked subprocess
Summary(pl.UTF-8):	Uruchamianie każdego testu w oddzielnym procesie
Name:		python-pytest-forked
Version:	1.3.0
Release:	6
License:	MIT
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/pytest-forked/
Source0:	https://files.pythonhosted.org/packages/source/p/pytest-forked/pytest-forked-%{version}.tar.gz
# Source0-md5:	7de04c46b48ca5c5a24e45bf1546355f
URL:		https://github.com/pytest-dev/pytest-forked
BuildRequires:	python-modules >= 1:2.7
BuildRequires:	python-setuptools >= 1:41.4
BuildRequires:	python-setuptools_scm >= 3.3
%if %{with tests}
BuildRequires:	python-py
BuildRequires:	python-pytest >= 3.10
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python-modules >= 1:2.7
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Run each test in a forked subprocess.

%description -l pl.UTF-8
Uruchamianie każdego testu w oddzielnym procesie.

%package -n python3-pytest-forked
Summary:	Run each test in a forked subprocess
Summary(pl.UTF-8):	Uruchamianie każdego testu w oddzielnym procesie
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.5

%description -n python3-pytest-forked
Run each test in a forked subprocess.

%description -n python3-pytest-forked -l pl.UTF-8
Uruchamianie każdego testu w oddzielnym procesie.

%prep
%setup -q -n pytest-forked-%{version}

%build
%py_build

%if %{with tests}
# pytest-flaky plugin breaks test_functional_boxed_capturing;
# test_xfail relies on plugin autoloading, so can't PYTEST_DISABLE_PLUGIN_AUTOLOAD=1
PYTHONPATH=$(pwd)/src \
%{__python} -m pytest -p no:flaky testing
%endif

%install
rm -rf $RPM_BUILD_ROOT

%py_install

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG LICENSE README.rst example/boxed.txt
%{py_sitescriptdir}/pytest_forked
%{py_sitescriptdir}/pytest_forked-%{version}-py*.egg-info
