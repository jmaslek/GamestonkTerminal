import React, { SVGProps } from "react"
interface SVGRProps {
  title?: string
  titleId?: string
}

const SupportIcon = ({
  title,
  titleId,
  ...props
}: SVGProps<SVGSVGElement> & SVGRProps) => (
  <svg
    viewBox="0 0 27 28"
    width={27}
    height={28}
    fill="none"
    xmlns="http://www.w3.org/2000/svg"
    aria-labelledby={titleId}
    {...props}
  >
    {title ? <title id={titleId}>{title}</title> : null}
    <path
      d="M15.59 27.333h-4.853a1.333 1.333 0 0 1-1.303-1.048l-.543-2.512a10.67 10.67 0 0 1-2.046-1.183l-2.45.78a1.333 1.333 0 0 1-1.56-.604L.403 18.565a1.341 1.341 0 0 1 .258-1.652l1.9-1.734a10.799 10.799 0 0 1 0-2.362l-1.9-1.73a1.341 1.341 0 0 1-.258-1.653L2.83 5.23a1.333 1.333 0 0 1 1.56-.604l2.45.78c.325-.241.663-.464 1.014-.667.336-.19.683-.361 1.037-.514l.544-2.51A1.333 1.333 0 0 1 10.737.666h4.853c.626 0 1.168.437 1.301 1.05l.55 2.51a10.676 10.676 0 0 1 2.045 1.183l2.45-.78a1.333 1.333 0 0 1 1.56.604l2.426 4.204c.31.543.203 1.228-.257 1.652l-1.9 1.733a10.8 10.8 0 0 1 0 2.363l1.9 1.733c.46.423.567 1.109.257 1.652l-2.427 4.204a1.333 1.333 0 0 1-1.558.604l-2.451-.78a10.653 10.653 0 0 1-2.045 1.181l-.55 2.506a1.333 1.333 0 0 1-1.301 1.048Zm-8.267-7.695 1.094.8c.246.182.503.349.769.5.25.145.508.277.772.395l1.244.545.61 2.788h2.706l.61-2.79 1.243-.545a8.198 8.198 0 0 0 1.538-.888l1.094-.8 2.722.867 1.353-2.344-2.11-1.924.149-1.35a8.038 8.038 0 0 0 0-1.775l-.15-1.35L23.08 9.84l-1.354-2.345-2.722.867-1.094-.8a8.305 8.305 0 0 0-1.538-.895l-1.244-.545-.609-2.788h-2.707L11.2 6.122l-1.241.544a7.918 7.918 0 0 0-.772.39c-.264.152-.52.318-.765.498l-1.095.8-2.72-.867L3.25 9.84l2.11 1.922-.149 1.35a8.04 8.04 0 0 0 0 1.776l.15 1.35L3.25 18.16l1.353 2.344 2.72-.867Zm5.835-.305a5.333 5.333 0 1 1 5.333-5.334 5.34 5.34 0 0 1-5.333 5.334Zm0-8a2.667 2.667 0 1 0 2.667 2.786v.534-.654a2.667 2.667 0 0 0-2.667-2.666Z"
      fill="currentColor"
    />
  </svg>
)

export default SupportIcon