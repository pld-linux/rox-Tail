%define _name Tail
%define _platform %(echo `uname -s`-`uname -m|sed 's/i.86/ix86/'`)
Summary:	Display the contents of file, updating as the file is updated
Summary(pl):	ROX-Tail wy¶wietla zawarto¶æ pliku, aktualizuj±c j± gdy plik siê zmieni
Name:		rox-%{_name}
Version:	2.1.2
Release:	1
License:	GPL v2
Group:		X11/Applications
Source0:	http://www.kerofin.demon.co.uk/rox/%{_name}-%{version}.tar.gz
# Source0-md5:	d5243ccebe206c4173efe6eff3e47d28
Source1:	%{name}.desktop
#Patch0:		%{name}-paths-fix.patch
Patch1:		%{name}-ROX-CLib2-include.patch
Patch2:		%{name}-ROX-apps-paths.patch
Patch3:		%{name}-aclocal.patch
URL:		http://www.kerofin.demon.co.uk/rox/tail.html
BuildRequires:	autoconf
BuildRequires:	gtk+2-devel
BuildRequires:	rox-CLib2-devel >= 2.1.4
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_appsdir	%{_libdir}/ROX-apps

%description
This program displays the contents of a file in a read-only text
window, updating as the file is updated. It is designed to do the same
function as the "tail -f" command.

%description -l pl
Ten program wy¶wietla zawarto¶æ pliku, w oknie "tylko-do-odczytu",
aktualizuj±c j± gdy plik siê zmieni. Program pe³ni t± sam± funkcjê co
komenda "tail -f".

%prep
%setup -q -n %{_name}
#%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
cd src
%{__autoconf}
cd ..
./AppRun --compile

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_appsdir}/%{_name}/{Help,%{_platform}}
install -d $RPM_BUILD_ROOT{%{_desktopdir},%{_pixmapsdir}}

install .DirIcon *.xml AppRun rox_run $RPM_BUILD_ROOT%{_appsdir}/%{_name}
install Help/README $RPM_BUILD_ROOT%{_appsdir}/%{_name}/Help
install %{_platform}/Tail $RPM_BUILD_ROOT%{_appsdir}/%{_name}/%{_platform}
install .DirIcon $RPM_BUILD_ROOT%{_pixmapsdir}/rox-Tail.png
install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Help/{Changes,Versions}
%attr(755,root,root) %dir %{_appsdir}
%attr(755,root,root) %{_appsdir}/%{_name}/*[Rr]un
%attr(755,root,root) %{_appsdir}/%{_name}/%{_platform}
%{_appsdir}/%{_name}/.DirIcon
%{_appsdir}/%{_name}/*.xml
%{_appsdir}/%{_name}/Help
%dir %{_appsdir}/%{_name}
%{_desktopdir}/%{name}.desktop
%{_pixmapsdir}/%{name}.png
