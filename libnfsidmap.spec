%define	major 0
%define libname	%mklibname nfsidmap %{major}
%define _disable_ld_no_undefined 1

Summary:	Library to help mapping id's, mainly for NFSv4
Name:		libnfsidmap
Version:	0.25
Release:	1
License:	BSD-like
Group:		System/Libraries
URL:		http://www.citi.umich.edu/projects/nfsv4/linux/
Source0:	http://www.citi.umich.edu/projects/nfsv4/linux/libnfsidmap/libnfsidmap-%{version}.tar.gz
BuildRequires:	openldap-devel
BuildRequires:	openssl-devel
BuildRequires:	pkgconfig

%description
libnfsidmap is a library holding mulitiple methods of mapping
names to id's and visa versa, mainly for NFSv4. 

When NFSv4 is using AUTH_GSS (which currently only supports
Kerberos v5), the NFSv4 server mapping functions MUST use
secure communications.

%package -n	%{libname}
Summary:	Library to help mapping id's, mainly for NFSv4
Group:		System/Libraries
Provides:	libnfsidmap
Provides:	nfsidmap

%description -n	%{libname}
libnfsidmap is a library holding mulitiple methods of mapping
names to id's and visa versa, mainly for NFSv4. 

When NFSv4 is using AUTH_GSS (which currently only supports
Kerberos v5), the NFSv4 server mapping functions MUST use
secure communications.

%package -n	%{libname}-devel
Summary:	Static library and header files for the nfsidmap library
Group:		Development/C
Requires:	%{libname} >= %{version}
Provides:	libnfsidmap-devel = %{version}
Provides:	nfsidmap-devel  = %{version}

%description -n	%{libname}-devel
libnfsidmap is a library holding mulitiple methods of mapping
names to id's and visa versa, mainly for NFSv4. 

When NFSv4 is using AUTH_GSS (which currently only supports
Kerberos v5), the NFSv4 server mapping functions MUST use
secure communications.

This package contains the static libnfsidmap library and its
header files.

%prep
%setup -q -n %{name}-%{version}

%build
%configure2_5x
%__make

%install
rm -rf %{buildroot}

%makeinstall_std

# cleanups
rm -f %{buildroot}%{_libdir}/*.*a

%files -n %{libname} 
%doc AUTHORS ChangeLog COPYING README
%{_libdir}/*.so.%{major}*
%{_libdir}/%{name}
%{_mandir}/man3/*
%{_mandir}/man5/*

%files -n %{libname}-devel
%doc AUTHORS ChangeLog COPYING README
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/libnfsidmap.pc
