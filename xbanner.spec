Name:		xbanner
Summary:	A program for customizing the look of the standard XDM interface
Version:	1.31
Release:	%mkrel 23
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


