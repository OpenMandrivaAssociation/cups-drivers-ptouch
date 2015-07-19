%define rname ptouch

Summary:	CUPS/foomatic driver for Brother P-touch label printers
Name:		cups-drivers-%{rname}
Version:	1.3
Release:	16
License:	GPLv2
Group:		System/Printing
URL:		http://www.diku.dk/~panic/P-touch/
Source0:	http://www.diku.dk/~panic/P-touch/%{rname}-driver-%{version}.tar.gz
BuildRequires:	cups-devel
BuildRequires:	ghostscript
Requires:	cups

%description
The ptouch-driver consists of a CUPS raster filter for driving the family of
Brother P-touch label printers.

This package contains CUPS foomatic drivers for the following printers:

%prep
%setup -qn %{rname}-driver-%{version}

%build
export CC=gcc
%configure \
	--libdir=%{_prefix}/lib

%make

%install
install -d %{buildroot}%{_datadir}/cups/model/%{rname}

%makeinstall_std

%files
%doc AUTHORS COPYING ChangeLog NEWS README
%{_prefix}/lib/cups/filter/rastertoptch
%{_datadir}/foomatic/db/source/printer/*.xml
%{_datadir}/foomatic/db/source/driver/*.xml
%{_datadir}/foomatic/db/source/opt/*.xml
%dir %{_datadir}/cups/model/%{rname}

