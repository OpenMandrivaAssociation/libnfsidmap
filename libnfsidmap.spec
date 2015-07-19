%define	major	0
%define libname	%mklibname nfsidmap %{major}
%define devname	%mklibname nfsidmap -d
%bcond_with	crosscompile

Summary:	Library to help mapping id's, mainly for NFSv4
Name:		libnfsidmap
Version:	0.25
Release:	11
License:	BSD-like
Group:		System/Libraries
Url:		http://www.citi.umich.edu/projects/nfsv4/linux/
Source0:	http://www.citi.umich.edu/projects/nfsv4/linux/libnfsidmap/%{name}-%{version}.tar.gz
BuildRequires:	openldap-devel
BuildRequires:	pkgconfig(openssl)

%description
libnfsidmap is a library holding mulitiple methods of mapping
names to id's and visa versa, mainly for NFSv4. 

When NFSv4 is using AUTH_GSS (which currently only supports
Kerberos v5), the NFSv4 server mapping functions MUST use
secure communications.

%package -n	%{libname}
Summary:	Library to help mapping id's, mainly for NFSv4
Group:		System/Libraries

%description -n	%{libname}
libnfsidmap is a library holding mulitiple methods of mapping
names to id's and visa versa, mainly for NFSv4. 

When NFSv4 is using AUTH_GSS (which currently only supports
Kerberos v5), the NFSv4 server mapping functions MUST use
secure communications.

%package -n	%{devname}
Summary:	Development library and header files for the nfsidmap library
Group:		Development/C
Requires:	%{libname} >= %{version}-%{release}
Provides:	libnfsidmap-devel = %{version}-%{release}
Provides:	nfsidmap-devel  = %{version}-%{release}
Obsoletes:	%{_lib}nfsidmap0-devel < 0.25-3

%description -n	%{devname}
This package contains the development libnfsidmap library and its
header files.

%prep
%setup -q
autoreconf -fi
%if %{with crosscompile}
export ac_cv_func_malloc_0_nonnull=yes
%endif

%build
%configure2_5x \
	--disable-static \
	--with-pluginpath=%{_libdir}/%{name} \

%make

%install
%makeinstall_std

%files -n %{libname}
%{_libdir}/libnfsidmap.so.%{major}*
%dir %{_libdir}/%{name}
%{_libdir}/%{name}/nsswitch.so
%{_libdir}/%{name}/static.so
%{_libdir}/%{name}/umich_ldap.so

%files -n %{devname}
%doc AUTHORS ChangeLog COPYING README
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/libnfsidmap.pc
%{_mandir}/man3/*
%{_mandir}/man5/*

