%define rname ptouch

Summary:	CUPS/foomatic driver for Brother P-touch label printers
Name:		cups-drivers-%{rname}
Version:	1.5
Release:	2
License:	GPLv2
Group:		System/Printing
URL:		https://github.com/trialinfo/ptouch-driver
Source0:	https://github.com/trialinfo/ptouch-driver/archive/refs/tags/v%{version}.tar.gz
BuildRequires:	cups-devel
BuildRequires:	ghostscript
BuildRequires:	perl(XML::LibXML)
BuildRequires:	pkgconfig(libpng)
Requires:	cups

%description
The ptouch-driver consists of a CUPS raster filter for driving the family of
Brother P-touch label printers.

This package contains CUPS foomatic drivers for the following printers:

%prep
%autosetup -p1 -n %{rname}-driver-%{version}
autoheader
%configure \
	--libdir=%{_prefix}/lib

%build
%make_build

%install
install -d %{buildroot}%{_datadir}/cups/model/%{rname}

%make_install

# Fix dupe from foomatic-db
rm -f %{buildroot}%{_datadir}/foomatic/db/source/printer/Brother-PT-2300.xml

%files
%doc AUTHORS COPYING ChangeLog NEWS README
%{_prefix}/lib/cups/filter/rastertoptch
%{_datadir}/foomatic/db/source/printer/*.xml
%{_datadir}/foomatic/db/source/driver/*.xml
%{_datadir}/foomatic/db/source/opt/*.xml
%dir %{_datadir}/cups/model/%{rname}

