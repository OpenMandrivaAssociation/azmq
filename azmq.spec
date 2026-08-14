%define devname %mklibname -d azmq

Summary: C++ language binding library integrating ZeroMQ with Boost Asio
Name: azmq
Version: 1.0.3
Release: 5
Url: https://github.com/zeromq/azmq
Source0: https://github.com/zeromq/azmq/archive/v%{version}/%{name}-%{version}.tar.gz
Group: System/Libraries
License: Boost
BuildRequires: cmake
BuildRequires: ninja
BuildRequires: pkgconfig(libzmq)
BuildRequires: boost-devel
# Headers-only library
BuildArch: noarch

%patchlist
azmq-1.0.3-boost-1.86.patch

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
# Boost 1.92 removed asio/io_service.hpp (use io_context)
find . -type f \( -name '*.hpp' -o -name '*.cpp' \) -print0 | xargs -0 sed -i \
	-e 's|<boost/asio/io_service.hpp>|<boost/asio/io_context.hpp>|g' \
	-e 's|boost::asio::io_service::work \([A-Za-z0-9_]*\)(\([^)]*\))|auto \1 = boost::asio::make_work_guard(\2)|g' \
	-e 's|boost::asio::io_service|boost::asio::io_context|g' \
	-e 's|asio::io_service|asio::io_context|g' \
	-e 's|get_io_service()|get_io_context()|g' \
	-e 's|io_service_|io_context_|g'
# make_work_guard lives in this header
grep -rl make_work_guard --include='*.cpp' --include='*.hpp' . | xargs -r sed -i \
	-e '/io_context.hpp/a\
#include <boost/asio/executor_work_guard.hpp>'
%cmake -G Ninja

%build
%ninja_build -C build

%install
%ninja_install -C build

%files -n %{devname}
%{_includedir}/azmq
