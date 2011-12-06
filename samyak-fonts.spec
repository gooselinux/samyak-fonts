%define	fontname	samyak
%global fontconf	67-%{fontname}
%define langlist	"devanagari gujarati tamil malayalam oriya"

# Common description
%define common_desc \
The Samyak package contains fonts for the display of \
Scripts Devanagari, Gujarati, Malayalam, Oriya and Tamil

Name:	 %{fontname}-fonts
Version:	1.2.1
Release:	9%{?dist}
Summary:	Free Indian truetype/opentype fonts
Group:	User Interface/X
License:	GPLv3+ with exceptions
URL:	http://sarovar.org/projects/samyak/
# Source0: http://sarovar.org/frs/?group_id=461&release_id=821
Source:	samyak-fonts-%{version}.tar.gz
Source1: 67-samyak-devanagari.conf
Source2: 67-samyak-tamil.conf
Source3: 68-samyak-malayalam.conf
Source4: 67-samyak-gujarati.conf
Source5: 67-samyak-oriya.conf
BuildArch:	noarch
BuildRequires:	fontpackages-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%description
%common_desc

%package common
Summary:  Common files for samyak-fonts
Group:	User Interface/X
Requires: fontpackages-filesystem
Provides: %{fontname}-common-fonts = %{version}-%{release}
Obsoletes: %{fontname}-common-fonts < 1.2.1-4
%description common
%common_desc

%package -n %{fontname}-devanagari-fonts
Summary: Open Type Fonts for Devanagari script
Group: User Interface/X 
Requires: %{name}-common = %{version}-%{release}
License: GPLv3+ with exceptions
Provides: %{name}-devanagari = %{version}-%{release}
Obsoletes: %{name}-devanagari < 1.2.1-3
%description -n %{fontname}-devanagari-fonts
This package contains truetype/opentype font for the display of \
Scripts Devanagari.

%_font_pkg -n devanagari -f %{fontconf}-devanagari.conf %{fontname}-devanagari/Samyak-*.ttf 

%package -n %{fontname}-tamil-fonts
Summary: Open Type Fonts for Tamil script
Group: User Interface/X 
Requires: %{name}-common = %{version}-%{release}
License: GPLv3+ with exceptions
Provides: %{name}-tamil = %{version}-%{release}
Obsoletes: %{name}-tamil < 1.2.1-3
%description -n %{fontname}-tamil-fonts
This package contains truetype/opentype font for the display of \
Scripts Tamil.

%_font_pkg -n tamil -f %{fontconf}-tamil.conf %{fontname}-tamil/*.ttf 

%package -n %{fontname}-malayalam-fonts
Summary: Open Type Fonts for Malayalam script
Group: User Interface/X 
Requires: %{name}-common = %{version}-%{release}
License: GPLv3+ with exceptions
Provides: %{name}-malayalam = %{version}-%{release}
Obsoletes: %{name}-malayalam < 1.2.1-3
%description -n %{fontname}-malayalam-fonts
This package contains truetype/opentype font for the display of \
Scripts Malayalam.

%_font_pkg -n malayalam -f 68-samyak-malayalam.conf %{fontname}-malayalam/*.ttf 

%package -n %{fontname}-gujarati-fonts
Summary: Open Type Fonts for Gujarati script
Group: User Interface/X 
Requires: %{name}-common = %{version}-%{release}
License: GPLv3+ with exceptions
Provides: %{name}-gujarati = %{version}-%{release}
Obsoletes: %{name}-gujarati < 1.2.1-3
%description -n %{fontname}-gujarati-fonts
This package contains truetype/opentype font for the display of \
Scripts Gujarati.

%_font_pkg -n gujarati -f %{fontconf}-gujarati.conf %{fontname}-gujarati/*.ttf 

%package -n %{fontname}-oriya-fonts
Summary: Open Type Fonts for Oriya script
Group: User Interface/X 
Requires: %{name}-common = %{version}-%{release}
License: GPLv3+ with exceptions
Provides: %{name}-oriya = %{version}-%{release}
Obsoletes: %{name}-oriya < 1.2.1-3
%description -n %{fontname}-oriya-fonts
This package contains truetype/opentype font for the display of \
Scripts Oriya.

%_font_pkg -n oriya -f %{fontconf}-oriya.conf %{fontname}-oriya/*.ttf 


%prep
%setup -q -n samyak-fonts-%{version}

%build
echo "Nothing to do in Build."

%install
rm -rf %{buildroot}

for i in "%{langlist}"
do
install -m 0755 -d %{buildroot}%{_fontdir}/samyak-$i
install -m 0644 -p $i/* %{buildroot}%{_fontdir}/samyak-$i
done

install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
		%{buildroot}%{_fontconfig_confdir}

# Repeat for every font family
install -m 0644 -p %{SOURCE1} \
	%{buildroot}%{_fontconfig_templatedir}/%{fontconf}-devanagari.conf

install -m 0644 -p %{SOURCE2} \
	%{buildroot}%{_fontconfig_templatedir}/%{fontconf}-tamil.conf

install -m 0644 -p %{SOURCE3} \
	%{buildroot}%{_fontconfig_templatedir}/68-samyak-malayalam.conf

install -m 0644 -p %{SOURCE4} \
	%{buildroot}%{_fontconfig_templatedir}/%{fontconf}-gujarati.conf

install -m 0644 -p %{SOURCE5} \
	%{buildroot}%{_fontconfig_templatedir}/%{fontconf}-oriya.conf


for fconf in %{fontconf}-devanagari.conf \
		%{fontconf}-tamil.conf \
		68-samyak-malayalam.conf \
		%{fontconf}-gujarati.conf \
		%{fontconf}-oriya.conf ; do
  ln -s %{_fontconfig_templatedir}/$fconf \
	%{buildroot}%{_fontconfig_confdir}/$fconf
done

%clean
rm -fr %{buildroot}


%files common
%defattr(-,root,root,-) 
%doc COPYING README AUTHORS
%dir %{_fontdir}

%changelog
* Tue May 04 2010 Pravin Satpute <psatpute@redhat.com> - 1.2.1-9
- Resolves: bug 586846

* Thu Feb 25 2010 Pravin Satpute <psatpute@redhat.com> 1.2.1-8
- Resolves: bug 568256

* Wed Feb 24 2010 Pravin Satpute <psatpute@redhat.com> 1.2.1-7
- added fontconf files for each subpackage
- Resolves: bug 567614

* Mon Nov 30 2009 Dennis Gregorovic <dgregor@redhat.com> - 1.2.1-6.1
- Rebuilt for RHEL 6

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Feb 04 2009 Pravin Satpute <psatpute@redhat.com> 1.2.1-4
- renamed samyak-common-fonts to samyak-fonts-common

* Tue Feb 03 2009 Pravin Satpute <psatpute@redhat.com> 1.2.1-3
- renamed font package as per fedora new Font_package_naming guideline
- updated spec

* Mon Jan 12 2009 Pravin Satpute <psatpute@redhat.com> 1.2.1-2
- bugzilla 477451
- updated spec

* Thu Sep 18 2008 Pravin Satpute <psatpute@redhat.com> 1.2.1-1
- upstream release 1.2.1
- Added Unicode 5.1 support in Samyak-Devanagari 

* Fri Apr 04 2008 Pravin Satpute <psatpute@redhat.com> 1.2.0-2
- given proper license name
- fc-cache now run on samyak-langname folder

* Thu Feb 28 2008 Pravin Satpute <psatpute@redhat.com> - 1.2.0-1
- update to samyak-fonts-1.2.0 from upstream cvs
- major bug fixes for devanagari and malayalam
- licence update to 'GNU Gplv3 or later with font exceptions'
- update spec file

* Fri Feb 08 2008 Pravin Satpute <psatpute@redhat.com> - 1.1.0-2
- added sub packaging support in spec file based on lohit-fonts.spec file 

* Fri Jan 18 2008 Pravin Satpute <psatpute@redhat.com> - 1.1.0-1
- initial packaging
