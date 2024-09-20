fun gauss(x: Int, y: Int, omega: Int, a: Int, b: Int): Double {
    var first = 1 / (2 * Math.PI * (omega * omega))
    var second = Math.pow(Math.E, (-((x - a) * (x - a) + (y - b) * (y - b)) / (2 * omega * omega)).toDouble())
    var res = (first as Double * second)
    return res
}

fun gausianBlur(mat: Array<Array<Double>>, kernelSize: Int, devation: Int): Array<Array<Double>> {
    var kernel = Array<Array<Double>>(kernelSize) { row -> Array<Double>(3) { column -> 1.0 } }
    val a = (kernelSize + 1) / 2 as Int
    val b = a
    var res = mat
    for (i in 0..kernelSize-1)
    {
        for (j in 0..kernelSize-1)
        {
            kernel[i][j]=gauss(i,j,devation,a,b)
        }
    }

    val sum = kernel.flatMap { it.asIterable() }.sum()

    for (i in 0..kernelSize-1)
    {
        for (j in 0..kernelSize-1)
        {
            kernel[i][j]/=sum
        }
    }
    var start=(kernelSize/2).toInt()
    for (i in start..mat.size-1)
    {
        for (j in start..mat[0].size-1)
        {
            var value=0.0
            for(k in -start..start-1)
            {
                for(l in -start..start-1)
                {
                    value+=mat[i+k][j+l]*kernel[k+start][l+start]
                }
            }
            res[i][j]=value
        }
    }

    return res
}


fun main(args: Array<String>) {
   var blur= gausianBlur(arrayOf(
        arrayOf(35.0,35.0,35.0,27.0,26.0,23.0,23.0,37.0,40.0),
        arrayOf(37.0,7.0,13.0,53.0,44.0,52.0,34.0,36.0,38.0),
        arrayOf(110.0,116.0,172.0,143.0,187.0,172.0,223.0,115.0,115.0),
        arrayOf(12.0,7.0,84.0,66.0,92.0,74.0,11.0,12.0,13.0),
        arrayOf(232.0,244.0,200.0,215.0,235.0,234.0,233.0,192.0,193.0),
        arrayOf(35.0,35.0,35.0,27.0,26.0,23.0,23.0,37.0,40.0),
        arrayOf(37.0,7.0,13.0,53.0,44.0,52.0,34.0,36.0,38.0),
        arrayOf(110.0,116.0,172.0,143.0,187.0,172.0,223.0,115.0,115.0),
        arrayOf(12.0,7.0,84.0,66.0,92.0,74.0,11.0,12.0,13.0),
        arrayOf(232.0,244.0,200.0,215.0,235.0,234.0,233.0,192.0,193.0)), 3, 100)
    for (row in blur)
    {
        for (element in row)
        {
            print("["+element+"] ")
        }
        print("\n")
    }
}