%global pypi_name text-unidecode

Name:           python-%{pypi_name}
Version:        1.3
Release:        1%{?dist}
Summary:        The most basic Text::Unidecode port
Group:          Development/Python
License:        Artistic License
URL:            https://github.com/kmike/text-unidecode/
Source0:        https://github.com/kmike/text-unidecode/archive/refs/tags/%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python-setuptools
BuildRequires:	python-pytest

%description
Text-Unidecode text-unidecode is the most basic port of the Text::Unidecode <
Perl library.There are other Python ports of Text::Unidecode (unidecode_ and
isounidecode_). unidecode_ is GPL; isounidecode_ uses too much memory, and it
didn't support Python 3 when this package was created.You can redistribute it
and/or modify this port under the terms of either the Artistic License, GPL
or GPLv2+

%prep
%autosetup -n %{pypi_name}-%{version}

# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%check
export PYTHONPATH=%{buildroot}%{python3_sitelib}:$PYTHONPATH
%{__python3} -m pytest

%files -n python-%{pypi_name}
%license LICENSE
%doc README.rst
%{python3_sitelib}/text_unidecode
%{python3_sitelib}/text_unidecode-%{version}-py%{python3_version}.egg-info

%changelog
* Tue Oct 21 2025 Samuil Ivanov <samuil.ivanovbg@gmail.com> - 1.3-1
- Updated spec to use Python 3.11
- Verified tests run correctly with Python 3.11
