Summary:	GUI interface to convert a physical machine to run as virtual machine on KVM
Summary(pl.UTF-8):	Graficzny interfejs do konwersji maszyny fizycznej na maszynę wirtualną KVM
Name:		virt-p2v
Version:	1.42.3
Release:	1
License:	GPL v2+
Group:		Applications/System
Source0:	https://download.libguestfs.org/virt-p2v/%{name}-%{version}.tar.gz
# Source0-md5:	549a1c253a05ba03e42800cdd5126120
URL:		https://libguestfs.org/
BuildRequires:	bash-completion-devel >= 1:2.0
BuildRequires:	dbus-devel
BuildRequires:	glib2-devel >= 1:2.56
BuildRequires:	gtk+3-devel >= 3.22
BuildRequires:	libxml2-devel >= 2.0
BuildRequires:	pcre2-8-devel
BuildRequires:	perl-List-MoreUtils
BuildRequires:	perl-modules
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Virt-p2v is a GUI interface to convert a physical machine to run as
virtual machine on KVM.

%description -l pl.UTF-8
Virt-p2v to graficzny interfejs do konwertowania maszyn fizycznych,
aby działały jako maszyny wirtualne KVM.

%prep
%setup -q

%build
%configure \
	--disable-silent-rules
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# useless in binary package
%{__rm} $RPM_BUILD_ROOT%{_mandir}/man1/p2v-{building,hacking}.1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS README
%attr(755,root,root) %{_bindir}/virt-p2v-make-disk
%attr(755,root,root) %{_bindir}/virt-p2v-make-kickstart
%attr(755,root,root) %{_bindir}/virt-p2v-make-kiwi
%{_libdir}/virt-p2v
%{_datadir}/virt-p2v
%{bash_compdir}/virt-p2v-make-disk
%{bash_compdir}/virt-p2v-make-kickstart
%{bash_compdir}/virt-p2v-make-kiwi
%{_mandir}/man1/p2v-release-notes.1*
%{_mandir}/man1/virt-p2v.1*
%{_mandir}/man1/virt-p2v-make-disk.1*
%{_mandir}/man1/virt-p2v-make-kickstart.1*
%{_mandir}/man1/virt-p2v-make-kiwi.1*
