Summary:	Binary firmware for the Poulsbo (psb) 3D X11 driver
Name:		psb-firmware
Version:	0.30
Release:	4%{?dist}
License:	Redistributable, no modification permitted
Group:		System Environment/Kernel
URL:		http://ppa.launchpad.net/ubuntu-mobile/ubuntu/pool/main/p/psb-firmware/
Source0:	http://ppa.launchpad.net/ubuntu-mobile/ubuntu/pool/main/p/psb-firmware/%{name}_%{version}.orig.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:	noarch

Requires:	kernel
# Arch switch obsolete
Obsoletes:	psb-firmware < 0.30-3

%description
This package contains the binary firmware for the Poulsbo (psb) 3D X11
driver.

%prep
%setup -q -n %{name}

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/lib/firmware
install -m 0644 msvdx_fw.bin %{buildroot}/lib/firmware

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc COPYING
/lib/firmware/msvdx_fw.bin

%changelog
* Wed Sep 30 2009 Adam Williamson <adamwill AT shaw DOT ca> - 0.30-4
- change my email address in changelog to correct one for Fusion

* Thu Aug 20 2009 Adam Williamson <adamwill AT shaw DOT ca> - 0.30-3
- switch to noarch

* Wed Aug 19 2009 Adam Williamson <adamwill AT shaw DOT ca> - 0.30-2
- correct license for RPMFusion conventions

* Mon Aug 10 2009 Adam Williamson <adamwill AT shaw DOT ca> - 0.30-1
- begin changelog tracking

