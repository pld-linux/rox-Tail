%define _name Tail
%define _platform %(echo `uname -s`-`uname -m|sed 's/i.86/ix86/'`)
Summary:	Display the contents of file, updating as the file is updated
Summary(pl):	ROX-Tail wy¶wietla zawarto¶æ pliku, aktualizuj±c j± gdy plik siê zmieni
Name:		rox-%{_name}
Version:	1.2.1
Release:	2
License:	GPL
Group:		X11/Applications
Source0:	http://www.kerofin.demon.co.uk/rox/%{_name}-%{version}.tgz
# Source0-md5:	9c281dd5432e89bdcbe8843192aa18ee
Patch0:		%{name}-paths-fix.patch
URL:		http://www.kerofin.demon.co.uk/rox/utils.html#tail
BuildRequires:	rox-CLib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define   _appsdir  %{_libdir}/ROX-apps

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
%patch0 -p1

%build
./AppRun --compile

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_appsdir}/%{_name}/{Help,%{_platform}}

rm -f ../install
install App* rox_run $RPM_BUILD_ROOT%{_appsdir}/%{_name}
install Help/README $RPM_BUILD_ROOT%{_appsdir}/%{_name}/Help
install %{_platform}/Tail $RPM_BUILD_ROOT%{_appsdir}/%{_name}/%{_platform}

%clean
rm -rf $RPM_BUILD_ROOT
rm -f install

%files
%defattr(644,root,root,755)
%doc Help/Versions
%attr(755,root,root) %{_appsdir}/%{_name}/*[Rr]un
%attr(755,root,root) %{_appsdir}/%{_name}/%{_platform}
%{_appsdir}/%{_name}/AppI*
%{_appsdir}/%{_name}/Help
%dir %{_appsdir}/%{_name}
