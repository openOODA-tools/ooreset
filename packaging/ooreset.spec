Name:           ooreset
Version:        0.1.0
Release:        1%{?dist}
Summary:        Emergency terminal hardware state reset restoring sane cooked-mode and cursor posture.
License:        ASL 2.0
URL:            https://github.com/openOODA-tools/ooreset
Source0:        ooreset-linux-x86_64
Source1:        uninstall.sh
BuildArch:      x86_64
Requires:       glibc

%description
ooreset is a sovereign, capability-bounded TERMINAL RESTORE written
in pure openOODA, featuring zero ambient authority, oote color themes,
and an MCP stdio server.

%install
mkdir -p %{buildroot}/usr/bin
install -m 0755 %{SOURCE0} %{buildroot}/usr/bin/ooreset
install -m 0755 %{SOURCE1} %{buildroot}/usr/bin/ooreset-uninstall

%files
/usr/bin/ooreset
/usr/bin/ooreset-uninstall

%changelog
* Wed Oct 07 2026 openOODA-tools <ops@openooda.org> - 0.1.0-1
- Initial sovereign blueprint scaffolding
