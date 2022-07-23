%define devname %mklibname -d azmq

Summary: C++ language binding library integrating ZeroMQ with Boost Asio
Name: azmq
Version: 1.0.2
Release: 2
Url: https://github.com/zeromq/azmq
Source0: https://github.com/zeromq/azmq/archive/v%{version}/%{name}-%{version}.tar.gz
Patch0: azmq-1.0.2-clang-libstdc++.patch
Patch1: https://github.com/zeromq/azmq/commit/0eef114987a0edb80eb8b94d302ac40c83514e92.patch
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
%autosetup -p1
%cmake -G Ninja

%build
%ninja_build -C build

%install
%ninja_install -C build

%files -n %{devname}
%{_includedir}/azmq
