# Created by pyp2rpm-3.3.5
%global pypi_name text-unidecode

Name:           python-%{pypi_name}
Version:        1.3
Release:        1
Summary:        The most basic Text::Unidecode port
Group:          Development/Python
License:        Artistic License
URL:            https://github.com/kmike/text-unidecode/
Source0:        %{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)

%description
Text-Unidecode text-unidecode is the most basic port of the Text::Unidecode <
Perl library.There are other Python ports of Text::Unidecode (unidecode_ and
isounidecode_). unidecode_ is GPL; isounidecode_ uses too much memory, and it
didn't support Python 3 when this package was created.You can redistribute it
and/or modify this port under the terms of either:* Artistic License_, or * GPL
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
%{__python3} setup.py test

%files -n python-%{pypi_name}
%license LICENSE
%doc README.rst
%{python3_sitelib}/text_unidecode
%{python3_sitelib}/text_unidecode-%{version}-py%{python3_version}.egg-info

