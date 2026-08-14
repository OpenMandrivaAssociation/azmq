%define devname %mklibname -d azmq

Summary: C++ language binding library integrating ZeroMQ with Boost Asio
Name: azmq
Version: 1.1.0
Release: 1
Url: https://github.com/zeromq/azmq
# 1.1.0 is untagged; snapshot with Boost >= 1.87 Asio io_context port
Source0: https://github.com/zeromq/azmq/archive/819b24035c.tar.gz#/%{name}-%{version}.tar.gz
Group: System/Libraries
License: Boost
BuildRequires: cmake
BuildRequires: ninja
BuildRequires: pkgconfig(libzmq)
BuildRequires: boost-devel
# Headers-only library
BuildArch: noarch

%description
C++ language binding library integrating ZeroMQ with Boost Asio

%package -n %{devname}
Summary: C++ language binding library integrating ZeroMQ with Boost Asio
Group: Development/C++ and C
Provides: azmq-devel = %{EVRD}
Requires: pkgconfig(libzmq)
Requires: boost-devel

%description -n %{devname}
C++ language binding library integrating ZeroMQ with Boost Asio

%prep
%autosetup -p1 -n azmq-819b24035cfa5b73081e21f5867445f2344f680d
# No network in the buildroot; skip tests/docs that would FetchContent Catch2
%cmake -G Ninja -DAZMQ_BUILD_TESTS=OFF -DAZMQ_BUILD_DOC=OFF -DAZMQ_DEVELOPER=OFF

%build
%ninja_build -C build

%install
%ninja_install -C build

%files -n %{devname}
%{_includedir}/azmq
%{_prefix}/lib/cmake/azmq
