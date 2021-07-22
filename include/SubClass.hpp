
#include "BaseClass.hpp"

namespace sphinx_test {

/**
 * This is some class
 * @tparam T_A  Template 1
 * @tparam T_B  Template 3
 */
template <typename T_A, typename T_B>
AR_DDS_RPC_EXPORT class [[deprecated(
"This is a deprecated class and you should not use it!")]] SubClass
    : public BaseClass<T_A, T_B>
{

}

}