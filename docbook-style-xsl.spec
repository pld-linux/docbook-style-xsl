Summary:	Modular DocBook Stylesheets
Summary(es):	Norman Walsh's modular stylesheets for DocBook
Summary(pl):	Arkusze stylistyczne XSL dla DocBook DTD
Summary(pt_BR):	Stylesheets modulares do Norman Walsh para DocBook
Name:		docbook-style-xsl
Version:	1.50.0
Release:	2
License:	(C) 1997, 1998 Norman Walsh (Free)
Group:		Applications/Publishing/XML
Vendor:		Norman Walsh http://nwalsh.com/
Source0:	http://prdownloads.sourceforge.net/docbook/docbook-xsl-%{version}.tar.gz
URL:		http://docbook.sourceforge.net/projects/xsl/index.html
Requires:	libxml2 >= 2.4.21-6
BuildArch:	noarch
AutoReqProv:	0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
XSL is a stylesheet language for both print and online rendering.
There is XSL stylesheets for DocBook DTD.

%description -l es
These XSL stylesheets allow to produce XSL FO trees or HTML / XHTML
with any DocBook XML document. They are highly customizable.

%description -l pl
docbook-xsl jest zbiorem arkuszy stylistycznych pozwalaj±cych
przekszta³ciæ dokument napisany w DocBook DTD na prezentacjê on-line
(wykorzystuj±c HTML) lub na drukowany dokument.

%description -l pt_BR
Stylesheets modulares do Norman Walsh para DocBook.

%prep
%setup -q -n docbook-xsl-%{version}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/sgml/docbook/xsl-stylesheets-%{version} \
	$RPM_BUILD_ROOT%{_javaclassdir}

cp -a * $RPM_BUILD_ROOT%{_datadir}/sgml/docbook/xsl-stylesheets-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%post
for f in fo html xhtml; do
	%{_bindir}/xmlcatalog --noout --add rewriteSystem \
		http://docbook.sourceforge.net/release/xsl/%{version}/$f/docbook.xsl \
		file://%{_datadir}/sgml/docbook/xsl-stylesheets-%{version}/$f/docbook.xsl \
		/etc/xml/catalog
done

%postun
for f in fo html xhtml; do
	%{_bindir}/xmlcatalog --noout --del \
		http://docbook.sourceforge.net/release/xsl/%{version}/$f/docbook.xsl \
		/etc/xml/catalog
done

%files
%defattr(644,root,root,755)
%doc doc ChangeLog WhatsNew BUGS TODO README
%dir %{_datadir}/sgml/docbook/xsl-stylesheets-%{version}
#%attr(755,root,root) %{_datadir}/sgml/docbook/xsl-stylesheets-%{version}/bin/*.pl
%{_datadir}/sgml/docbook/xsl-stylesheets-%{version}/VERSION
%{_datadir}/sgml/docbook/xsl-stylesheets-%{version}/common
#%{_datadir}/sgml/docbook/xsl-stylesheets-%{version}/contrib
#%{_datadir}/sgml/docbook/xsl-stylesheets-%{version}/doc
#%{_datadir}/sgml/docbook/xsl-stylesheets-%{version}/docsrc
%{_datadir}/sgml/docbook/xsl-stylesheets-%{version}/extensions
%{_datadir}/sgml/docbook/xsl-stylesheets-%{version}/fo
%{_datadir}/sgml/docbook/xsl-stylesheets-%{version}/html
%{_datadir}/sgml/docbook/xsl-stylesheets-%{version}/images
#%{_datadir}/sgml/docbook/xsl-stylesheets-%{version}/indexing
%{_datadir}/sgml/docbook/xsl-stylesheets-%{version}/javahelp
%{_datadir}/sgml/docbook/xsl-stylesheets-%{version}/lib
%{_datadir}/sgml/docbook/xsl-stylesheets-%{version}/template
%{_datadir}/sgml/docbook/xsl-stylesheets-%{version}/xhtml
