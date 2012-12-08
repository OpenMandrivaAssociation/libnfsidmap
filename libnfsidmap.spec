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


%changelog
* Mon May 02 2011 Oden Eriksson <oeriksson@mandriva.com> 0.24-2mdv2011.0
+ Revision: 661503
- mass rebuild

* Fri Dec 10 2010 Guillaume Rousse <guillomovitch@mandriva.org> 0.24-1mdv2011.0
+ Revision: 620451
- update to new version 0.24

* Thu Nov 25 2010 Oden Eriksson <oeriksson@mandriva.com> 0.23-3mdv2011.0
+ Revision: 601057
- rebuild

* Sun Mar 14 2010 Oden Eriksson <oeriksson@mandriva.com> 0.23-2mdv2010.1
+ Revision: 519027
- rebuild

* Sun Aug 30 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.23-1mdv2010.0
+ Revision: 422543
- new version
- drop plugin patch, merged upstream

* Sun Aug 23 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.22-1mdv2010.0
+ Revision: 419901
- new version
- merge two patches

  + Christophe Fergeau <cfergeau@mandriva.com>
    - make sure autoreconf update libtool files to avoid libtool 1.5/2.2 mismatches

* Thu Dec 18 2008 Oden Eriksson <oeriksson@mandriva.com> 0.21-3mdv2009.1
+ Revision: 315579
- rebuild

* Mon Sep 08 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.21-2mdv2009.0
+ Revision: 282812
- fix lib64 (bug #43666)

* Sat Sep 06 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.21-1mdv2009.0
+ Revision: 281960
- new version
  patch for isolating plugins under %%{_libdir}/%%{name}

* Sat Jun 28 2008 Oden Eriksson <oeriksson@mandriva.com> 0.20-4mdv2009.0
+ Revision: 229895
- fix linkage

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Mon Dec 24 2007 Oden Eriksson <oeriksson@mandriva.com> 0.20-2mdv2008.1
+ Revision: 137469
- rebuilt against openldap-2.4.7 libs

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Mon Apr 23 2007 Andreas Hasenack <andreas@mandriva.com> 0.20-1mdv2008.0
+ Revision: 17634
- updated to version 0.20


* Mon Jan 22 2007 Andreas Hasenack <andreas@mandriva.com> 0.19-1mdv2007.0
+ Revision: 111810
- updated to version 0.19

  + Oden Eriksson <oeriksson@mandriva.com>
    - bzip2 cleanup

* Wed Oct 11 2006 Oden Eriksson <oeriksson@mandriva.com> 0.16-2mdv2007.1
+ Revision: 63381
- bunzip patches
- Import libnfsidmap

* Wed Jun 07 2006 Oden Eriksson <oeriksson@mandriva.com> 0.16-1mdv2007.0
- 0.16
- fix deps

* Fri Mar 03 2006 Oden Eriksson <oeriksson@mandriva.com> 0.13-1mdk
- 0.13
- the upstream source was renamed to libnfsidmap, obey that

* Sun Dec 18 2005 Stefan van der Eijk <stefan@eijk.nu> 0.11-2mdk
- fix provides

* Sat Dec 17 2005 Stefan van der Eijk <stefan@eijk.nu> 0.11-1mdk
- 0.11
- rediffed patch0

* Wed Aug 31 2005 Buchan Milne <bgmilne@linux-mandrake.com> 0.10-2mdk
- Rebuild for libldap2.3

* Sun Feb 27 2005 Oden Eriksson <oeriksson@mandrakesoft.com> 0.10-1mdk
- 0.10

* Tue Feb 08 2005 Buchan Milne <bgmilne@linux-mandrake.com> 0.8-6mdk
- fix deps

* Tue Feb 08 2005 Buchan Milne <bgmilne@linux-mandrake.com> 0.8-5mdk
- really build against new openldap
- rename srpm and spec so we can use rpmbuildupdate

* Fri Feb 04 2005 Oden Eriksson <oeriksson@mandrakesoft.com> 0.8-4mdk
- rebuilt against new openldap libs

* Sun Jan 09 2005 Oden Eriksson <oeriksson@mandrakesoft.com> 0.8-3mdk
- drop S1 & S2, these belong to the nfs-utils package

* Sun Jan 09 2005 Oden Eriksson <oeriksson@mandrakesoft.com> 0.8-2mdk
- make it compile on 10.0 too

* Sun Jan 09 2005 Oden Eriksson <oeriksson@mandrakesoft.com> 0.8-1mdk
- 0.8

* Wed Oct 27 2004 Oden Eriksson <oeriksson@mandrakesoft.com> 0.5-1mdk
- initial mandrake contrib

