#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : nvme-cli
Version  : 1.2
Release  : 6
URL      : http://github.com/linux-nvme/nvme-cli/archive/v1.2.tar.gz
Source0  : http://github.com/linux-nvme/nvme-cli/archive/v1.2.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0
Requires: nvme-cli-bin
Requires: nvme-cli-data
Requires: nvme-cli-doc
Patch1: build.patch

%description
nvmetests
=========
This contains NVMe unit tests framework. The purpose of this framework
to use nvme cli and test various supported commands and scenarios for
NVMe device.

%package bin
Summary: bin components for the nvme-cli package.
Group: Binaries
Requires: nvme-cli-data

%description bin
bin components for the nvme-cli package.


%package data
Summary: data components for the nvme-cli package.
Group: Data

%description data
data components for the nvme-cli package.


%package doc
Summary: doc components for the nvme-cli package.
Group: Documentation

%description doc
doc components for the nvme-cli package.


%prep
%setup -q -n nvme-cli-1.2
%patch1 -p1

%build
export LANG=C
export SOURCE_DATE_EPOCH=1490219886
make V=1  %{?_smp_mflags}

%install
export SOURCE_DATE_EPOCH=1490219886
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/nvme

%files data
%defattr(-,root,root,-)
/usr/share/bash_completion.d/nvme

%files doc
%defattr(-,root,root,-)
%doc /usr/share/man/man1/*
