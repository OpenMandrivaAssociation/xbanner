Name:		xbanner
Summary:	A program for customizing the look of the standard XDM interface
Version:	1.31
Release:	27
License:	GPL
Group:		Graphical desktop/Other
BuildRequires: X11-devel xpm-devel imake

Url:		http://www.hijinks.com/~spade/linux/XBanner/
Source:		ftp://physics.fullerton.edu/pub/Linux/XBanner/XBanner1.31.tar.bz2
Source1:	XBanner.mdkdefaults.bz2
Source2:	xdm_bg.xpm.bz2
Patch:		xbanner-1.3-rh.patch
Patch1:		XBanner-asnonroot.patch

Buildroot:	%{_tmppath}/xbanner-root

%description
The XBanner program allows the display of text, patterns and images
in the root window, so users can customize the XDM style login screen
and/or the normal X background.

Install XBanner if you'd like to change the look of your X login screen
and/or X background.

%prep
%setup -q -n XBanner1.31
%patch -p1 -b .patch
%patch1 -p0

%build
xmkmf -a
make

%install
rm -rf $RPM_BUILD_ROOT

mkdir -p $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr
mkdir -p $RPM_BUILD_ROOT/usr/X11R6/bin
mkdir -p $RPM_BUILD_ROOT/usr/X11R6/include/X11/pixmaps
mkdir -p $RPM_BUILD_ROOT/usr/X11R6/lib/X11/app-defaults

for i in xbanner freetemp xb_check;do
install -c  --strip --mode "0755"  $i $RPM_BUILD_ROOT/usr/X11R6/bin/$i
done

bzcat %{SOURCE1} > $RPM_BUILD_ROOT/usr/X11R6/lib/X11/app-defaults/XBanner
bzcat %{SOURCE2} > $RPM_BUILD_ROOT/usr/X11R6/include/X11/pixmaps/xdm_bg.xpm

# fixup bogus permissions
chmod -R og+rX $RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
# I left random_effect out because the default "make install" rule doesn't
# install it
#
# (fg) Added %defattr - whois "I" above? :)
#/usr/X11R6/bin/random_effect

/usr/X11R6/bin/*
/usr/X11R6/include/X11/pixmaps/xdm_bg.xpm
/usr/X11R6/lib/X11/app-defaults/XBanner
%defattr(0644,root,root,755)
%doc ToDo QuickStart index.html docs
%doc samples docs/*




%changelog
* Wed Dec 08 2010 Oden Eriksson <oeriksson@mandriva.com> 1.31-26mdv2011.0
+ Revision: 615492
- the mass rebuild of 2010.1 packages

* Sat Feb 20 2010 Funda Wang <fwang@mandriva.org> 1.31-25mdv2010.1
+ Revision: 508723
- rediff patch

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild

* Sun Aug 03 2008 Thierry Vignaud <tv@mandriva.org> 1.31-24mdv2009.0
+ Revision: 262255
- rebuild

* Thu Jul 31 2008 Thierry Vignaud <tv@mandriva.org> 1.31-23mdv2009.0
+ Revision: 256587
- rebuild

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 1.31-21mdv2008.1
+ Revision: 136576
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request
    - buildrequires X11-devel instead of XFree86-devel


* Wed Nov 22 2006 Lenny Cartier <lenny@mandriva.com> 1.31-21mdv2007.0
+ Revision: 86218
- Adjust buildrequires
- Import xbanner

