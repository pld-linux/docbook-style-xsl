Summary:	Modular DocBook Stylesheets
Summary(pl):	Arkusze stylistyczne XSL dla DocBook DTD
Name:		docbook-style-xsl
%define		ver 1
%define		subver 29
Version:	%{ver}.%{subver}
Release:	3
Copyright:	(C) 1997, 1998 Norman Walsh (Free)
Group:		Applications/Publishing/XML
Group(pl):	Aplikacje/Publikowanie/XML
Vendor:		Norman Walsh http://nwalsh.com/
Source0:	http://nwalsh.com/docbook/xsl/dbx%{ver}%{subver}.zip
URL:		http://nwalsh.com/docbook/xsl/index.html
Requires:	sgml-common >= 0.5
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
#BuildRequires:	perl
BuildArch:	noarch
AutoReqProv:    0

# do weryfikacji:

#XSL is a stylesheet language for both print and online rendering.
#There is XSL stylesheets for DocBook DTD.

#docbook-xsl jest zbiorem arkuszy stylistycznych pozwalaj±cych
#przekszta³ciæ dokument napisany w DocBook DTD na prezentacjê
#on-line (wykorzystuj±c HTML) lub na drukowany dokument.

%description

%description -l pl

%prep
%setup -q -c -T
unzip -qa %{SOURCE0}
mv docbook/* .
rmdir docbook

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/sgml/docbook/xsl-stylesheets-%{version} 

# remove indexing as it confuses xt :( /klakier
grep -v '<xsl:include href="index.xsl"/>' html/docbook.xsl > html/docbook.xsl.tmp
mv -f html/docbook.xsl.tmp html/docbook.xsl
grep -v '<xsl:include href="index.xsl"/>' fo/docbook.xsl > fo/docbook.xsl.tmp
mv -f fo/docbook.xsl.tmp fo/docbook.xsl

cp -a * $RPM_BUILD_ROOT%{_datadir}/sgml/docbook/xsl-stylesheets-%{version} 

gzip -9nf ChangeLog WhatsNew BUGS TODO README

%clean
rm -rf $RPM_BUILD_ROOT

%post
ln -sfn xsl-stylesheets-%{version} %{_datadir}/sgml/docbook/xsl-stylesheets

%preun
if [ "$1" = 0 ]; then
rm -f %{_datadir}/sgml/docbook/xsl-stylesheets
fi


%files
%defattr(644,root,root,755)
%doc test doc {ChangeLog,WhatsNew,BUGS,TODO,README}.gz
%attr(755,root,root) %{_datadir}/sgml/docbook/xsl-stylesheets-%{version}/bin/*.pl
%{_datadir}/sgml/docbook/xsl-stylesheets-%{version}/VERSION
%{_datadir}/sgml/docbook/xsl-stylesheets-%{version}/common
%{_datadir}/sgml/docbook/xsl-stylesheets-%{version}/contrib
#%{_datadir}/sgml/docbook/xsl-stylesheets-%{version}/doc
#%{_datadir}/sgml/docbook/xsl-stylesheets-%{version}/docsrc
%{_datadir}/sgml/docbook/xsl-stylesheets-%{version}/extensions
%{_datadir}/sgml/docbook/xsl-stylesheets-%{version}/fo
%{_datadir}/sgml/docbook/xsl-stylesheets-%{version}/html
%{_datadir}/sgml/docbook/xsl-stylesheets-%{version}/images
%{_datadir}/sgml/docbook/xsl-stylesheets-%{version}/indexing
%{_datadir}/sgml/docbook/xsl-stylesheets-%{version}/javahelp
%{_datadir}/sgml/docbook/xsl-stylesheets-%{version}/lib
%{_datadir}/sgml/docbook/xsl-stylesheets-%{version}/template
%{_datadir}/sgml/docbook/xsl-stylesheets-%{version}/xhtml
