%define	major 0
%define libname	%mklibname nfsidmap %{major}

Summary:	Library to help mapping id's, mainly for NFSv4
Name:		libnfsidmap
Version:	0.20
Release:	%mkrel 3
License:	BSD-like
Group:		System/Libraries
URL:		http://www.citi.umich.edu/projects/nfsv4/linux/
Source0:	http://www.citi.umich.edu/projects/nfsv4/linux/libnfsidmap/libnfsidmap-%{version}.tar.gz
Patch0:		nfsidmap-0.11-portable.diff
BuildRequires:	openldap-devel
BuildRequires:	openssl-devel
BuildRequires:	automake1.7
BuildRequires:	autoconf2.5
BuildRequires:	pkgconfig
BuildRequires:	libtool
BuildRoot:	%{_tmppath}/%{name}-%{version}-root

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
Requires:	%{libname} = %{version}
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
%patch0 -p0

%build
export WANT_AUTOCONF_2_5=1
rm -f configure
libtoolize --copy --force && aclocal-1.7 && autoconf && automake-1.7 --gnu

%configure2_5x

%make

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%makeinstall_std

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%endif

%if %mdkversion < 200900
%postun -n %{libname} -p /sbin/ldconfig
%endif

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files -n %{libname} 
%defattr(-,root,root)
%doc AUTHORS ChangeLog COPYING README
%{_libdir}/*.so.*
%{_mandir}/man3/*

%files -n %{libname}-devel
%defattr(-,root,root)
%doc AUTHORS ChangeLog COPYING README
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/*.a
%{_libdir}/*.la
%{_libdir}/pkgconfig/libnfsidmap.pc


