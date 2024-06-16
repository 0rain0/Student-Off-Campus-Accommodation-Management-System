<template>
    <form action="http://127.0.0.1:5000/receive_form_t" method="POST">
        <table>
            <tr>
                <th colspan="8" class="center"><h1>校外賃居訪視記錄-導師填寫</h1></th>
            </tr>
        </table>

        <table>
            <tr>
                <th colspan="2" class="line">環境及作息評估（導師填寫）</th>
            </tr>
            <tr>
                <th class="evaluate">押金要求</th>
                <td>
                    <div class="radio-group">
                        <label><input type="radio" name="EN_01" value="0" :checked="student.EN_01 === 0"> 合理</label>
                        <label><input type="radio" name="EN_01" value="1" :checked="student.EN_01 === 1"> 不合理（2個月以上之租金）</label>
                    </div>
                </td>
            </tr>

            <tr>
                <th class="evaluate">水電費要求</th>
                <td>
                    <div class="radio-group">
                        <label><input type="radio" name="EN_02" value="0" :checked="student.EN_02 === 0"> 合理</label>
                        <label><input type="radio" name="EN_02" value="1" :checked="student.EN_02 === 1"> 不合理</label>
                    </div>
                </td>
            </tr>

            <tr>
                <th class="evaluate">居住環境</th>
                <td>
                    <div class="radio-group">
                        <label><input type="radio" name="EN_03" value="0" :checked="student.EN_03 === 0"> 佳</label>
                        <label><input type="radio" name="EN_03" value="1" :checked="student.EN_03 === 1"> 適中</label>
                        <label><input type="radio" name="EN_03" value="2" :checked="student.EN_03 === 2"> 欠佳，說明：<input type="text" name="EN_03_Des" size="20" :value="student.EN_03_Des"></label>
                    </div>
                </td>
            </tr>

            <tr>
                <th class="evaluate">生活設施</th>
                <td>
                    <div class="radio-group">
                        <label><input type="radio" name="EN_04" value="0" :checked="student.EN_04 === 0"> 佳</label>
                        <label><input type="radio" name="EN_04" value="1" :checked="student.EN_04 === 1"> 適中</label>
                        <label><input type="radio" name="EN_04" value="2" :checked="student.EN_04 === 2"> 欠佳，說明：<input type="text" name="EN_04_Des" size="20" :value="student.EN_04_Des"></label>
                    </div>
                </td>
            </tr>

            <tr>
                <th class="evaluate">訪視現況</th>
                <td colspan="3">
                    <div class="radio-group">
                        <label><input type="radio" name="VI_01" value="0" :checked="student.VI_01 === 0"> 生活規律</label>
                        <label><input type="radio" name="VI_01" value="1" :checked="student.VI_01 === 1"> 適中</label>
                        <label><input type="radio" name="VI_01" value="2" :checked="student.VI_01 === 2"> 待加強，說明：<input type="text" name="VI_01_Des" size="20" :value="student.VI_01_Des"></label>
                    </div>
                </td>
            </tr>
            <tr>
                <th class="evaluate">主客相處</th>
                <td colspan="3">
                    <div class="radio-group">
                        <label><input type="radio" name="VI_02" value="0" :checked="student.VI_02 === 0"> 和睦</label>
                        <label><input type="radio" name="VI_02" value="1" :checked="student.VI_02 === 1"> 欠佳</label>
                    </div>
                </td>
            </tr>
        </table>

        <table>
            <tr>
                <th colspan="4" class="line">訪視結果（導師填寫）</th>
            </tr>
            <tr>
                <th colspan="4">
                    <div class="radio-group">
                        <label><input type="radio" name="Result" value="0" :checked="student.Result === 0"> 整體賃居狀況良好</label>
                        <label><input type="radio" name="Result" value="1" :checked="student.Result === 1"> 聯繫家長關注</label>
                        <label><input type="radio" name="Result" value="2" :checked="student.Result === 2"> 安全堪慮請協助</label>
                        <label><input type="radio" name="Result" value="3" :checked="student.Result === 3"> 其他，說明：<input type="text" name="RE_Des" size="20" :value="student.RE_Des"></label>
                    </div>
                </th>
            </tr>
            <tr>
                <th colspan="4">其他記載或建議事項：<input type="text" size="20" name="RE_Memo" :value="student.RE_Memo"></th>
            </tr>

            <tr>
                <th colspan="4" class="line">關懷宣導項目（懇請導師賃居訪視時多予關懷叮嚀）</th>
            </tr>
            <tr>
                <td colspan="4">
                    <div class="radio-group">
                        <label><input type="checkbox" name="DI_01" value="0" :checked="student.DI_01 === 0"> 交通安全</label>
                        <label><input type="checkbox" name="DI_02" value="0" :checked="student.DI_02 === 0"> 拒絕菸害</label>
                        <label><input type="checkbox" name="DI_03" value="0" :checked="student.DI_03 === 0"> 拒絕毒品</label>
                        <label><input type="checkbox" name="DI_04" value="0" :checked="student.DI_04 === 0"> 登革熱防治</label>
                        <label><input type="checkbox" name="DI_05" value="0" :checked="student.DI_05 === 0"> 其他，說明：<input type="text" name="DI_05_Des" size="20" :value="student.DI_05_Des"></label>
                    </div>
                </td>
            </tr>
        </table>
    </form>
</template>

<script setup lang="ts">
import { defineProps, ref, watch } from 'vue'

const props = defineProps({
    student: {
        type: Object,
        required: true
    }
})

watch(props.student, (newVal) => {
    console.log('Received student data in Form_T:', newVal)
})

const formT = ref(null)
</script>