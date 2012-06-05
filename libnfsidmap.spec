%define	major 0
%define libname	%mklibname nfsidmap %{major}

Summary:	Library to help mapping id's, mainly for NFSv4
Name:		libnfsidmap
Version:	0.25
Release:	2
License:	BSD-like
Group:		System/Libraries
URL:		http://www.citi.umich.edu/projects/nfsv4/linux/
Source0:	http://www.citi.umich.edu/projects/nfsv4/linux/libnfsidmap/libnfsidmap-%{version}.tar.gz
BuildRequires:	openldap-devel
BuildRequires:	openssl-devel
BuildRequires:	pkgconfig
#BuildRequires:	voms-devel

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
%configure2_5x \
    --disable-static \
    --with-pluginpath=%{_libdir}/%{name} \

#    --enable-gums

%make

%install
rm -rf %{buildroot}

%makeinstall_std

%files -n %{libname}
%doc AUTHORS ChangeLog COPYING README
%{_libdir}/*.so.%{major}*
%dir %{_libdir}/%{name}
%{_libdir}/%{name}/nsswitch.so
%{_libdir}/%{name}/static.so
%{_libdir}/%{name}/umich_ldap.so
%{_mandir}/man3/*
%{_mandir}/man5/*

%files -n %{libname}-devel
%doc AUTHORS ChangeLog COPYING README
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/libnfsidmap.pc
